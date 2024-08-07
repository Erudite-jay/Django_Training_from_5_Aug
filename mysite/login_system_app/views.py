from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User_data_model
from .Serializers import UserSerializer
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def print_hello(request):
    return render(request,'Login_System_app/hello.html')

def print(request):
    return HttpResponse("Hello i am print project -> app -> views")

@csrf_exempt
def all_user_data(request):
    if request.method =='GET':
        try:
            user_data = User_data_model.objects.all()
            serialized_data = UserSerializer(user_data,many=True)
            return JsonResponse(serialized_data.data,safe=False)
        except:
            return JsonResponse({"error":"Failed to fetch data"},status=500) 
    
    if request.method =='POST':
        input_data=json.loads(request.body)
        serialized_data = UserSerializer(data=input_data)

        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data.data,status=201)
        else:
            return JsonResponse(serialized_data.errors,status=400)

@csrf_exempt
def single_user_data(request,pk):
    if request.method =='GET':
        try:
            user_data=User_data_model.objects.get(pk=pk)
            serialized_data = UserSerializer(user_data)
            return JsonResponse(serialized_data.data,safe=False)
        
        except User_data_model.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404) 
    
    if request.method =='PUT':
        try:
            user_data=User_data_model.objects.get(pk=pk)
            input_data=json.loads(request.body)
            serialized_data = UserSerializer(user_data,data=input_data)

            if serialized_data.is_valid():
                serialized_data.save()
                return JsonResponse(serialized_data.data,status=200)

        except User_data_model.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
    
    if request.method =='DELETE':
        try:
            user_data=User_data_model.objects.get(pk=pk)
            user_data.delete()
            return JsonResponse({"message":"User deleted successfully"},status=204)
        
        except User_data_model.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        
    if request.method =='PATCH':
        try:
            single_user_data=User_data_model.objects.get(pk=pk)
            input_data=json.loads(request.body)
            serialized_data=UserSerializer(single_user_data,data=input_data,partial=True)
            if serialized_data.is_valid():
                serialized_data.save()
                return JsonResponse(serialized_data.data,status=200)
        except:
            return JsonResponse({"error":"Failed to update user data"},status=500)