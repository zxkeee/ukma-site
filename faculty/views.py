from django.shortcuts import render
from faculty.models import FacultyInfo

# Create your views here.

def index(request):
    info = FacultyInfo.objects.first()
    return render(request, 'faculty/index.html', {'info': info})
