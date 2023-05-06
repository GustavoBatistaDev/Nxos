from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from .mixins import ValidatorMixin
from django.contrib import messages
from .models import UserCustom
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.contrib.auth import login as auth_login,logout
from .active_account import ActiveAccount


class RegisterView(View):
    def get(self, request: HttpRequest, **kwargs ) -> HttpResponse:
        return render(request, 'authentication/register.html')
    

    def post(self, request: HttpRequest, **kwargs) -> HttpResponse:
        validate_data = ValidatorMixin.validate_data_is_empty(request)
        if validate_data:
            validate_password = ValidatorMixin.validate_password(validate_data)
            if validate_password:
               names_is_valid = ValidatorMixin.validate_names(request)
               if names_is_valid:
                    email_is_valid = ValidatorMixin.validate_email(request)
                    if email_is_valid:
                        data = ValidatorMixin.get_data(request)
                        user_exists =  UserCustom.objects.filter(
                                 email=data['email']
                            )
                        if not user_exists.exists():
                            try:
                                hash_password = urlsafe_base64_encode(force_bytes(data['password']))
                                new_user = UserCustom.objects.create(
                                        first_name=data['first_name'],
                                        last_name=data['last_name'],
                                        email=data['email'],
                                        password=hash_password,
                                        is_active=False
                                    )
                                
                               
                                messages.add_message(request, messages.ERROR, 'Registered! check your email.')
                                return ValidatorMixin.redirect_client('authentication:login') 

                            except Exception:
                                messages.add_message(request, messages.ERROR, 'Something went wrong! Try again.')
                                return ValidatorMixin.redirect_client('authentication:register')
                        messages.add_message(request, messages.ERROR, 'Use another email.')
                        return ValidatorMixin.redirect_client('authentication:register')
                    messages.add_message(request, messages.ERROR, 'Invalid email')
                    return ValidatorMixin.redirect_client('authentication:register')
               messages.add_message(request, messages.ERROR, 'Check the name and last name fields! ')
               return ValidatorMixin.redirect_client('authentication:register')
            messages.add_message(request, messages.ERROR, 'Invalid password. ')
            return ValidatorMixin.redirect_client('authentication:register')
        messages.add_message(request, messages.ERROR, 'No field can be null!')
        return ValidatorMixin.redirect_client('authentication:register')


class LoginView(View):
    def get(self, request: HttpRequest, **kwargs ) -> HttpResponse:
     
        return render(request, 'authentication/login.html')


def active_account(request: HttpResponse, uidb4, token) -> HttpResponse:

    User = get_user_model()
    uid = force_str(urlsafe_base64_decode(uidb4))

    user = User.objects.filter(pk=uid)

    if (user := user.first()) and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        auth_login(request, user)

        messages.add_message(request, messages.SUCCESS, 'Your account has been saved successfully' ) 
        return redirect(reverse('login'))

    else:
        messages.add_message(request, messages.ERROR, 'The url accessed is not valid' ) 
        return redirect(reverse('register'))
    