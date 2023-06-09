from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.signals import user_logged_in
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.http import HttpRequest
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import (
    GoogleSocialAuthSerializer,
    LoginSerializer,
    PasswordUpdateSerializer,
    RegisterSerializer,
    UpdateProfileSerializer,
)


class RegisterView(GenericAPIView):
    """
    Create an account

    Returns:

        new_user: A newly registered user
    """

    serializer_class = RegisterSerializer

    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate confirmation link
        confirmation_link = request.build_absolute_uri(
            reverse("confirm_registration", args=[user.pk])
        )

        # Send confirmation email
        send_mail(
            "Account Confirmation",
            f"""Welcome {user.username}!

            Thank you for creating an account on Autobiz
            
            Please confirm your account by clicking on the link below or copy and paste in your browser.
            
            {confirmation_link}
            
            Thank You.""",
            "mchladelola@gmail.com",
            [serializer.validated_data["email"]],
            fail_silently=False,
        )
        # line 34 & 35 can also be written as
        # if serializer.is_valid():
        # serializer.save()

        return Response(
            {
                "message": "Registered successfully, Please check your email for confirmation.",
                "status": True,
            },
            status=status.HTTP_201_CREATED,
        )


class ConfirmationView(GenericAPIView):
    serializer_class = LoginSerializer

    @csrf_exempt
    def post(self, request, user_id):
        user = get_user_model().objects.get(pk=user_id)
        user.is_active = True
        user.save()
        return Response(
            {"message": "Registration confirmed! You can now log in."},
            status=status.HTTP_200_OK,
        )


class LoginView(GenericAPIView):
    """
    Login with either Username or Email & Password to get Authentication tokens

    Args:

        Login credentials (_type_): username/password OR email/password

    Returns:

        message: success

        tokens: access and refresh

        user: user profile details
    """

    serializer_class = LoginSerializer

    def post(self, request: HttpRequest, **kwargs):
        serializer = self.serializer_class(data=request.data)
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

        serializer.validated_data["username"] = username__email

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

        refresh = RefreshToken.for_user(user)

        user_logged_in.send_robust(get_user_model(), user=user)

        return Response(
            {
                "status": True,
                "message": "Logged in successfully",
                "tokens": {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                },
                "user": {
                    "id": user.pk,
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


class DetailUpdateView(GenericAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"user": self.request.user}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class GoogleSocialAuthView(GenericAPIView):
    """
    Login with Google by providing Auth_token

    Args:
        Auth_token
    """

    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """

        POST with "auth_token"
        Send an id token from google to get user information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        data["status"]: True
        return Response(data, status=status.HTTP_200_OK)


class PasswordUpdateView(GenericAPIView):
    """
    Change password

    """

    permission_classes = [IsAuthenticated]
    serializer_class = PasswordUpdateSerializer

    def post(self, request, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data["password1"]

        try:
            password_validation.validate_password(password, request.user)
        except Exception as e:
            return Response(
                {"message": e, "status": False}, status=status.HTTP_403_FORBIDDEN
            )

        request.user.set_password(password)
        request.user.save()
        return Response(
            {"message": "Password updated successfully", "status": True},
            status=status.HTTP_200_OK,
        )


