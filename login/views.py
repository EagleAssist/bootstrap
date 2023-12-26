from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login  
from django.contrib.auth.hashers import check_password
from .models import CustomUser as User
from django.shortcuts import redirect

class LoginView(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        serializer = UserSerializer(data=request.data)        
        # if serializer.is_valid():
            # Perform authentication logic here (e.g., check username and password)
            # For simplicity, you can use Django's built-in authentication
        username = serializer.initial_data['username']
        password = serializer.initial_data['password']
            # user = authenticate(request, username=username, password=password)
            # Check if the user with the provided username exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'message': 'Invalid login credentials'}, status=401)
        
        
        if password == user.password:
            login(request, user)
            return redirect('/table/modellist/')
        else:
            return Response({'message': 'Invalid Login credentials'}, status=401)

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)