from django.urls import path
from faculty import views

app_name = 'faculty'
urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.departments, name='departments'),
]