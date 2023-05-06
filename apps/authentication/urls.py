from django.urls import path
from . import views


app_name = 'authentication'


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('active_account/<uidb4>/<token>/', views.active_account, name='active_account'),

   
]