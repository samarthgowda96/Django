from rest_framework import serializers
from employeeApp.models import Employees, Departments,Test

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Departments
        fields=('DepartmentId','DepartmentName')
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employees
        fields=('EmployeeId','EmployeeName','Department','DateofJoining','PhotoFileName')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Test
        fields=('name','shirtSize')