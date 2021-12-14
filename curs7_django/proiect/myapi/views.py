from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from myapi.models import Employee
from myapi.serializers import EmployeeSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer
