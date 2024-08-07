from django.urls import path
from . import views

urlpatterns =[
    path('hello/',views.print),
    path('',views.print_hello),
    path('all-user-data/',views.all_user_data),
    path('single-user-data/<int:pk>/',views.single_user_data),  # pk is primary key of the model User_data_model
]