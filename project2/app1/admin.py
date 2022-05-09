from django.contrib import admin
from .models import Emplyoee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
     list_display = ['eid', 'ename', 'eadd', 'esal', 'image']
admin.site.register(Emplyoee, EmployeeAdmin)