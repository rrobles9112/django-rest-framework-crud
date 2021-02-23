from rest_framework import serializers
from .models import Employees
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):  # create class to serializer model
    
    class Meta:
        model = Employees
        fields = ('employee_code', 'salary_per_hour', 'start_data', 'departament')


    