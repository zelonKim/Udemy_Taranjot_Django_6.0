from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer


class LoginAPIView(APIView):
    # Overriding Global Auth
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        id = request.data.get('username')
        pw = request.data.get('password')
        
        user = authenticate(username=id, password=pw)
        
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)    
            return Response({'token': token.key})
        
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        
        
class UserRegistration(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'User Created Successfully'}, status=status.HTTP_201_CREATED)
        
        
        
        

class LogoutAPIView(APIView):
    def post(self, request):
        request.auth.delete()
        return Response({"msg": "Logout Success"})
    
    