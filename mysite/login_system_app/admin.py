from django.contrib import admin
from .models import User_data_model

# Register your models here.

@admin.register(User_data_model)
class User_data(admin.ModelAdmin):
    list_display = ['id','username', 'age', 'mobile_number', 'email']