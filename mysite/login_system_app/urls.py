from django.urls import path
from . import views

urlpatterns =[
    path('hello/',views.print),
    path('',views.print_hello),
    path('all-user-data/',views.all_user_data) 
]