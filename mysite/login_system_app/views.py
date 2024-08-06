from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User_data_model
from .Serializers import UserSerializer
# Create your views here.

def print_hello(request):
    return render(request,'Login_System_app/hello.html')

def print(request):
    return HttpResponse("Hello i am print project -> app -> views")

def all_user_data(request):
    if request.method =='GET':
        try:
            user_data = User_data_model.objects.all()
            serialized_data = UserSerializer(user_data,many=True)
            return JsonResponse(serialized_data.data,safe=False)
        except:
            return JsonResponse({"error":"Failed to fetch data"},status=500)