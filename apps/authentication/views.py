from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from .mixins import DataClient
from django.contrib import messages
from .models import UserCustom



class Register(View):
    def get(self, request: HttpRequest, **kwargs ) -> HttpResponse:
        return render(request, 'authentication/register.html')
    

    def post(self, request: HttpRequest, **kwargs) -> HttpResponse:
        validate_data = DataClient.validate_data_is_empty(request)
        if validate_data:
            validate_password = DataClient.validate_password(validate_data)
            if validate_password:
               names_is_valid = DataClient.validate_names(request)
               if names_is_valid:
                   return HttpResponse('salvbar')
               messages.add_message(request, messages.ERROR, 'Check the name and last name fields! ')
               return DataClient.redirect_client('authentication:register')
            messages.add_message(request, messages.ERROR, 'Invalid password. ')
            return DataClient.redirect_client('authentication:register')
        messages.add_message(request, messages.ERROR, 'No field can be null!')
        return DataClient.redirect_client('authentication:register')


class Login(View):
    def get(self, request: HttpRequest, **kwargs ) -> HttpResponse:
        return render(request, 'authentication/login.html')

