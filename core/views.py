from django.contrib.auth import authenticate, get_user_model 
# TO RAISE VALIDATION ERROR
from django.core.exceptions import ValidationError
# TO VALIDATE THE EMAIL
from django.core.validators import validate_email
# from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import LoginSerializer, RegisterSerializer



class RegisterView(GenericAPIView):
    """
    Create an account

    Returns:

        new_user: A newly registered user
    """

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # line 34 & 35 can also be written as
        # if serializer.is_valid():
            # serializer.save()

        return Response(
            {
                "message": "Registered successfully",
                "status": True,
            },
            status=status.HTTP_201_CREATED,
        )
    


class LoginView(TokenObtainPairView):
    """
    Login with either Username or Email & Password to get Authentication tokens

    Args:

        Login credentials (_type_): username/password OR email/password

    Returns:

        message: success

        tokens: access and refresh

        user: user profile details
    """

    serializer_class = TokenObtainPairSerializer

    def post(self, request, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # This could be a username or email
        username__email, password = serializer.validated_data.values()

        try:
            # Check if the provided data is an email or username

            validate_email(username__email)
            username__email = (
                get_user_model().objects.get(email=username__email).get_username()
            )

        except (get_user_model().DoesNotExist, ValidationError):
            pass

        user = authenticate(request, username=username__email, password=password)

        if not user:
            return Response(
                {"message": "Email/Username or password is incorrect", "status": False},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # if not user.is_verified:
        #     return Response(
        #             {"message": "You must verify your email first", "status": False},
        #             status=status.HTTP_401_UNAUTHORIZED,
        #     )

        
        request.data["username"] = username__email


        tokens = super().post(request)
        return Response(
            {
                "status": True,
                "message": "Logged in successfully",
                "tokens": tokens.data,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
            },
            status=status.HTTP_200_OK,
        )


class RefreshView(TokenRefreshView):
    """
    To get new access token after the initial one expires or becomes invalid

    Args:
        refresh_token

    Returns:
        access_token
    """

    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        access_token = serializer.validated_data["access"]
        return Response(
            {"access": access_token, "status": True}, status=status.HTTP_200_OK
        )