from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from .mixins import DataClient


class Register(View):
    def get(self, request: HttpRequest, **kwargs ) -> HttpResponse:
        return render(request, 'authentication/register.html')
    
    def post(self, request: HttpRequest, **kwargs) -> HttpResponse:
        validate_data = DataClient.validate_data_is_empty(request)
        if validate_data:
            validate_password = DataClient.validate_password(validate_data)
            if validate_password:
                return HttpResponse('pode salvar no banco')
            return redirect('authentication:register')

        else:
             return HttpResponse('algum campo está vazio')

        
        return HttpResponse('dados incorretos')
        

        return HttpResponse(data.values())


class Login(View):
    def get(self, request: HttpRequest, **kwargs ) -> HttpResponse:
        return render(request, 'authentication/login.html')
