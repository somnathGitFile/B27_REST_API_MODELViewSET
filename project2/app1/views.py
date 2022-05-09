from django.shortcuts import render
from app1.serializer import EmployeeSerializer
from .models import Emplyoee
from rest_framework import viewsets

# Create your views here.
class Employeedetails(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Emplyoee.objects.all()