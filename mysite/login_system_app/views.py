from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello(request):
    return render(request,'Login_System_app/hello.html')

def print(request):
    return HttpResponse("Hello i am print project -> app -> views")