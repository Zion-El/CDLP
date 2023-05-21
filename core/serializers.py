from django.contrib.auth import get_user_model, password_validation
from django.db.utils import IntegrityError
from rest_framework import serializers
from .models import Member
from .utils import Google, register_social_user
from decouple import config
 


class RegisterSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    # ref_id = serializers.CharField(allow_blank=True, allow_null=True)
    country = serializers.CharField()


    def validate_password(self, value):
        try:
            password_validation.validate_password(value, None)
        except Exception as e:
                # raises an error and state the exception met as message
            raise serializers.ValidationError(
                {"message": e, "status": False},
            )

        return value
    

    def save(self, **kwargs):
        try:
            user = get_user_model().objects._create_user(**self.validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                detail={
                    "message": "User with provided credentials already exists",
                    "status": False,
                }
            )

        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['sex', 'bvn_no', 'street', 'city', 'state', 'dob']

    def save(self, **kwargs):
        user = self.context.get('user')
        member = Member.objects.get(id=user.id)
        for attr, value in self.validated_data.items():
            setattr(member, attr, value)

        member.save()
        return member
    
    
        


class PasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, attrs):
        if not attrs["password1"] == attrs["password2"]:
            raise serializers.ValidationError(
                    detail={"message": "The two password fields didn’t match.", "status": False}
            )
        
        user = self.context['user']

        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError(
                {"message": "Invalid old password"}
            )

        return super().validate(attrs)


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate(self, data):
        auth_token = data.get("auth_token")
        user_data = Google.validate(auth_token)

        try:
            user_data["sub"]
        except Exception as identifier:
            raise serializers.ValidationError({"message": str(identifier), "status": False})

        if user_data["aud"] != config("GOOGLE_CLIENT_ID"):
            raise serializers.ValidationError(
                    {"message": "Invalid credentials", "status": False}
            )

        email = user_data["email"]
        name = user_data["name"]

        return register_social_user(email=email, name=name)
