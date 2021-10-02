from django.conf.urls import url
from employeeApp import views

from django.urls import path, re_path

urlpatterns=[
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)/([a-z]+)$',views.departmentApi),
    url(r'^employees$',views.employeeApi),
    url(r'^test$',views.testApi)
]