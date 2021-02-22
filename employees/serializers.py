from rest_framework import serializers
from .models import Employees
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):  # create class to serializer model
    
    class Meta:
        model = Employees
        fields = ('employee_code', 'salary_per_hour', 'start_data', 'departament')



class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Employees.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')
    