from django.contrib.auth import get_user_model, password_validation
from django.db.utils import IntegrityError
from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    ref_id = serializers.CharField(allow_blank=True, allow_null=True)
    country = serializers.CharField()

    def validate_password(self, value):
        try:
            password_validation.validate_password(value, None)
        except Exception as e:
            raise serializers.ValidationError(
                # raises an error and state the exception met as message
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
