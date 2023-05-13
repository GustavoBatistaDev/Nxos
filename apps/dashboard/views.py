from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from authentication.models import UserCustom
from django.urls import reverse
from typing import Type
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from authentication.mixins import ValidatorMixin
from authentication.models import UserCustom
from .mixins import ValidatorProfileMixin
from .models import Projects


@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, 'dashboard/dashboard.html')


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, 'dashboard/profile.html')
    

    def post(self, request: HttpRequest,  *args, **kwargs) -> HttpResponse:
        data = ValidatorProfileMixin.get_data(request)
        user = UserCustom.objects.filter(email=data['email']).exclude(id=request.user.id)
        if user.exists():
            messages.add_message(request, messages.ERROR, 'Try another email.')
            return redirect('dashboard:profile')
        fullname_is_valid = ValidatorProfileMixin.validate_fullname(request)
        if fullname_is_valid:
            email_is_valid = ValidatorProfileMixin.validate_email(request) 
            if email_is_valid:
                mobile_is_valid = ValidatorProfileMixin.validate_mobile(request) 
                if mobile_is_valid:
                    address_is_valid = ValidatorProfileMixin.validate_address(request)
                    if address_is_valid:
                        request.user.fullname = data['fullname']
                        request.user.email = data['email']
                        request.user.address = data['address']
                        request.user.mobile = data['mobile'] 
                        request.user.photo = data['photo'] 
                        request.user.save()
                        messages.add_message(request, messages.SUCCESS, 'Successfully updated')
                        return redirect('dashboard:profile')
                    messages.add_message(request, messages.ERROR, 'Address is invalid')
                    return redirect('dashboard:profile')
                messages.add_message(request, messages.ERROR, 'Mobile is invalid')
                return redirect('dashboard:profile')
            messages.add_message(request, messages.ERROR, 'Email is invalid')
            return redirect('dashboard:profile')
        messages.add_message(request, messages.ERROR, 'Fullname is invalid')
        return redirect('dashboard:profile')

        
@method_decorator(login_required, name='dispatch')
class ProjectView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        projects = Projects.objects.filter(user=request.user.id).order_by('-id')
        return render(request, 'dashboard/project.html', context={'projects':projects})

    
    def post(self, request: HttpRequest, *args, **kwargs):
        title = request.POST.get('title' )
        body = request.POST.get('body' )
  
       
        if not body or not title:
            messages.add_message(request, messages.SUCCESS, 'Title and text fields cannot be null!')
            return redirect('dashboard:projects')
        user = UserCustom.objects.get(id=request.user.id)
        _ = Projects.objects.create(
            user=user,
            title=title,
            body=body
        )
        messages.add_message(request, messages.SUCCESS, 'Project created')
        return redirect('dashboard:projects')
    

@method_decorator(login_required, name='dispatch')
class ProjectEditView(View):
    def get(self, request: HttpRequest, id: int):
        project = Projects.objects.filter(id=id).first()
        return render(request, 'dashboard/edit.html', context={'project':project})


    def post(self, request: HttpRequest, id: int):
        title = request.POST.get('title' )
        body = request.POST.get('body')
        if not body or not title:
            messages.add_message(request, messages.SUCCESS, 'Title and text fields cannot be null!')
            return redirect('dashboard:projects')
        project = Projects.objects.filter(id=id).first()
        project.title = title
        project.body = body
        project.save()
        messages.add_message(request, messages.SUCCESS, 'Project edited')
        return redirect('dashboard:projects')
    

@method_decorator(login_required, name='dispatch')
class ProjectDeleteView(View):
    def get(self, request: HttpRequest, id: int):
        project = Projects.objects.filter(id=id).first()
        project.delete()
        messages.add_message(request, messages.SUCCESS, 'Project deleted')
        return redirect('dashboard:projects')

