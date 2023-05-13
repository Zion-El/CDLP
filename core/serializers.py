from rest_framework import serializers
from .models import Member


class MemberSignUpSerialization(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Member
        field = (
            'first_name',
            'last_name',
            'email',
            'Phone',
            'username',
        )
    def create(self, validated_data):
        member = Member.objects.create(
            first_name=validated_data['email'],
            last_name=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['username'],
            username=validated_data['email'],
        )
        member.set_password(validated_data['password'])
        member.save()
        return member
