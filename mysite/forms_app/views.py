from django.http import JsonResponse
from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return JsonResponse({"success":True})
        else:
            return JsonResponse({"error":form.errors})
    else:
        form=ContactForm()
    return render(request,'forms_app/contact.html',{'form':form})