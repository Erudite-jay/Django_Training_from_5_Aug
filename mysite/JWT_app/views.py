from django.shortcuts import render
from django.contrib.auth import authenticate,login
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            refresh=RefreshToken.for_user(user)
            return JsonResponse(
                {
                    "success": True,
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh)
                },
                status=200
            )
        else:
            return JsonResponse({"error":"Invalid credentials"},status=401)
    return render(request, 'jwt/login.html')