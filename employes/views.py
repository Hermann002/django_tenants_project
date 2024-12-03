from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

def index(request):
    employees = Employee.objects.all()

    if request.POST:
        name = request.POST.get('name')
        Employee.objects.create(name=name)
        employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})
