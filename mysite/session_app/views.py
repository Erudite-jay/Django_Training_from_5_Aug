from django.http import JsonResponse
from django.shortcuts import render
from .models import User

# Create your views here.

def login(request):
    if request.session.get('username'):
        return JsonResponse({
            "username": f"{request.session.get('username')} is already logged in"
        })
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        try:
            user=User.objects.get(username=username)
            if user.password == password:
                request.session['username']=username
                request.session.set_expiry(20)
                return JsonResponse(
                    {
                     'message': 'Login successful',
                    }
                )
        except User.DoesNotExist:
            return JsonResponse(
                {
                 'error': 'Invalid credentials',
                }
            )
    return render(request, 'session_app/login.html')