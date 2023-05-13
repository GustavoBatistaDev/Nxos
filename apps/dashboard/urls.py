from django.urls import path
from . import views


app_name = 'dashboard'


urlpatterns = [
    path('', views.DashboardView.as_view(), name="dashboard"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('projects/edit/<int:id>/', views.ProjectEditView.as_view(), name='edit'),
    path('projects/delete/<int:id>/', views.ProjectDeleteView.as_view(), name='delete')    

   
]