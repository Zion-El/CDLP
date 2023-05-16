from django.contrib.auth import authenticate, get_user_model 
# TO RAISE VALIDATION ERROR
from django.core.exceptions import ValidationError
# TO VALIDATE THE EMAIL
from django.core.validators import validate_email
# from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
# import requests



from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



class RegisterView(GenericAPIView):
    """
    Create an account

    Returns:

        new_user: A newly registered user
    """

    serializer_class = RegisterSerializer
    
    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()


        # Generate confirmation link
        confirmation_link = request.build_absolute_uri(reverse('confirm_registration', args=[user.id]))

        # Send confirmation email
        send_mail(
            'Account Confirmation',
            f'''Welcome {user.username}!

            Thank you for creating an account on Autobiz
            
            Please confirm your account by clicking on the link below or copy and paste in your browser.
            
            {confirmation_link}
            
            Thank You.''',
            'mchladelola@gmail.com',
            [serializer.validated_data['email']],
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
    @csrf_exempt
    def post(self, request, user_id):
        user = User.objects.get(pk=user_id)
        user.is_active = True
        user.save()
        return JsonResponse({'message': 'Registration confirmed! You can now log in.'})







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
    


class DetailUpdateView(GenericAPIView):
    serializer_class =  UpdateProfileSerializer
    permission_classes = [IsAuthenticated]
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data, context= {'user' : self.request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    
    def get_serializer_context(self):
        print(self.request.user)
        return {
            'user' : self.request.user
        }




# class PasswordUpdateView(UpdateAPIView):
#     queryset = Member.objects.all()
#     serializer_class = PasswordUpdateSerializer
#     permission_classes = [IsAuthenticated]

#     def update(self, request, *args, **kwargs):
#         user = self.get_object()
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         old_password = serializer.validated_data.get('old_password')
#         new_password = serializer.validated_data.get('new_password')

#         if not check_password(old_password, user.password):
#             return Response({'detail': 'Invalid old password'}, status=400)

#         user.set_password(new_password)
#         user.save()

#         return Response({'detail': 'Password updated successfully'})

