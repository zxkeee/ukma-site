from django.urls import path
from faculty import views

app_name = 'faculty'
urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.departments, name='departments'),
    path('departments/<int:id>/', views.departments_details, name='departments_details'),
]