from dataclasses import fields
from pyexpat import model
from .models import Emplyoee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emplyoee
        fields = '__all__'
