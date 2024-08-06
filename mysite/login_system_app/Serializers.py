from rest_framework import serializers
from .models import User_data_model

# class UserSerializer(serializers.Serializer):
#      username= serializers.CharField(max_length=255)
#      age= serializers.IntegerField()
#      mobile_number= serializers.CharField(max_length=10)
#      email= serializers.EmailField()

#model serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_data_model
        fields = ['id','username', 'age', 'mobile_number', 'email']

#serializer for create and update