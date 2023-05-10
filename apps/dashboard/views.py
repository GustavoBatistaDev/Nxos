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


@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/dashboard.html')


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/profile.html')
    
    def post(self, request, *args, **kwargs):
        data = ValidatorMixin.get_data(request=request)
        user = UserCustom.objects.filter(email=data['email']).exclude(id=request.user.id)
        if user.exists():
            messages.add_message(request, messages.ERROR, 'You cannot register with this email.')
            return render(request, 'dashboard/profile.html')
        
        request.user.first_name = data['first_name']
        request.user.last_name = data['last_name']
        request.user.fullname = data['fullname']
        request.user.email = data['email']
        request.user.mobile = data['mobile']
        request.user.address = data['address']
        request.user.save()
        messages.add_message(request, messages.SUCCESS, 'Data updated successfully!')
        return redirect('dashboard:profile')


