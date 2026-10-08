from django.urls import path
from exchange import views

app_name = "exchange"

urlpatterns = [
    path('', views.programs, name='programs'),
]