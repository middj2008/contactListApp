from django.shortcuts import render
import jwt
from rest_framework.generics import GenericAPIView
from .serializers import LoginSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from django.conf import settings
from django.contrib import auth


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data=request.data
        username=data.get('username','')
        password=data.get('password','')
        user = auth.authenticate(username=username, password=password)

        if user:
            # Give them a token...
            auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")
            # if you want to serialize more than one instance dont forget to pass many=True
            serializer = UserSerializer(user)
            # Send back as json once given the token
            data = {'user': serializer.data, 'token': auth_token}
            return Response(data, status=status.HTTP_200_OK) 

            # SEND RES
        return Response({'detail':'Invalid credential'}, status=status.HTTP_401_UNAUTHORIZED)    
