from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from employeeApp.models import Employees, Departments,Test
from employeeApp.serializers import DepartmentSerializer,EmployeeSerializer,TestSerializer

# Create your views here.
@csrf_exempt
## CRUD Operations on department table
def departmentApi(request,id=0,test=""):
    if request.method=="GET":
        departments=Departments.objects.all()
        departments_serializer= DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=="POST":
        department_data= JSONParser().parse(request)
        departments_serializer= DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('Added Sucessfully',safe=False)
        return JsonResponse('Failed to Add',safe=False)
    elif request.method=="PUT":
        department_data= JSONParser().parse(request)
        department= Departments.objects.get(DepartmentId= department_data['DepartmentId'])
        departments_serializer= DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('Update Sucessfully',safe=False)
        return JsonResponse('Failed to update',safe=False)
    elif request.method=="DELETE":
        print('ww',id,test)
        department= Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse('deleted Sucessfully',safe=False)
@csrf_exempt    
## CRUD Operations on employee table
def employeeApi(request,id=0,test=""):
    if request.method=="GET":
        employees=Employees.objects.all()
        employees_serializer= EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=="POST":
        employees_data= JSONParser().parse(request)
        employees_serializer= EmployeeSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse('Added Sucessfully',safe=False)
        return JsonResponse('Failed to Add',safe=False)
    elif request.method=="PUT":
        employees_data= JSONParser().parse(request)
        employee= Employees.objects.get(EmployeeId= employees_data['EmployeeId'])
        employee_serializer= EmployeeSerializer(employee,data=employees_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Update Sucessfully',safe=False)
        return JsonResponse('Failed to update',safe=False)
    elif request.method=="DELETE":
        print('working',id,test)
        employee= Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse('deleted Sucessfully',safe=False)
      
@csrf_exempt
def testApi(request):
    if request.method=="GET":
        persons= Test.objects.all()
        
        persons_serialzer= TestSerializer(persons,many=True)
        print(persons_serialzer.data)
        return JsonResponse(persons_serialzer.data,safe=False)
    elif request.method=="POST":
        persons_data= JSONParser().parse(request)
        
        persons_serialzer= TestSerializer(data=persons_data)
        """ if persons_serialzer.is_valid():
            p=persons_serialzer.save() """
        p= Test(name=persons_data['name'],shirtSize=persons_data['shirtSize'])
        p.save()
        print(p.get_shirtSize_display())

        return JsonResponse(p.get_shirtSize_display(),safe=False)
        #return JsonResponse('Failed',safe=False)




