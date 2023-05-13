
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from core.serializers import MemberSignUpSerialization
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Member
from rest_framework import generics



# Create your views here.

# HANDLING SIGNUP
class SignUp(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MemberSignUpSerialization(data=request.data)
        if serializer.is_valid():
            member = serializer.save()
            response_data = {
                'first_name': member.first_name,
                'last_name': member.last_name,
                'email': member.email,
                'phone': member.phone,
                'username': member.username
            }
            return Response(serializer.data, content_type='application/json')
        else:
            return Response(serializer.errors, status=400)
        

    def get(self, request, *args, **kwargs):
        return Response("Hello, world!")
        

    # def post(self, request, *args, **kwargs):
    #     serializer = MemberSignUpSerialization(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)


class Login(APIView):
    def post(self, request, *arg, **kwargs):
        pass