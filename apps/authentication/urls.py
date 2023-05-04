from django.urls import path
from . import views


app_name = 'authentication'


urlpatterns = [
    path('', views.register, name='register'),
    path('dashboard/', views.dash , name="dashboard")
   
]