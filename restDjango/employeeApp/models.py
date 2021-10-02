from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId= models.AutoField(primary_key=True)
    DepartmentName= models.CharField(max_length=500)
class Employees(models.Model):
    EmployeeId= models.AutoField(primary_key=True)
    EmployeeName= models.CharField(max_length=500)
    Department= models.CharField(max_length=500)
    DateofJoining= models.DateField()
    PhotoFileName= models.CharField(max_length=500)
 
class Test(models.Model):
     SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
)
     name= models.CharField(max_length=60)
     shirtSize= models.CharField(max_length=1,choices=SHIRT_SIZES)
class TestEmployee(models.Model):
    EmployeeId= models.AutoField(primary_key=True)
    EmployeeName= models.CharField(max_length=500)
    Department= models.CharField(max_length=500)
    DateofJoining= models.DateField()
    PhotoFileName= models.CharField(max_length=500)