from django.shortcuts import render
from faculty.models import FacultyInfo, Department

# Create your views here.

def index(request):
    info = FacultyInfo.objects.first()
    return render(request, 'faculty/index.html', {'info': info})

def departments(request):
    deps = Department.objects.all()
    return render(request, 'faculty/departments.html', {'departments': deps})
