from django.urls import path
from . import views


app_name = 'authentication'


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('active_account/<uidb4>/<token>/', views.ActiveAccountView.as_view(), name='active_account'),

   
]