from .models import Student
from app1.serializer import StudentSerializer
from rest_framework import viewsets


# Create your views here.
class StudentInfo(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    