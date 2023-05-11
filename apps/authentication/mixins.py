from django.http import HttpRequest
from django.shortcuts import redirect
from typing import Type
import re
from django.core.mail import send_mail


class ValidatorMixin:

  
    @classmethod
    def get_data(cls, request: HttpRequest, **kwargs) -> dict:
        data = {}
        first_name = request.POST.get('first_name') or ''
        last_name = request.POST.get('last_name') or ''
        email = request.POST.get('email_address') or ''
        password = request.POST.get('password') or ''
        password2 = request.POST.get('password2') or ''
        terms_and_conditions = request.POST.get('terms_and_conditions') or ''
        data['first_name'] = first_name
        data['last_name'] = last_name
        data['email'] = email
        data['password'] = password
        data['password2'] = password2
        data['terms_and_conditions'] = terms_and_conditions
       
        return data
    

    @classmethod
    def validate_data_is_empty(cls, request: HttpRequest) -> bool:
        data = cls.get_data(request)
        print(data)
        for i in data.values():
            match i:
                case '':
                    return False
                case _:
                    continue
        return data 
    

    @classmethod
    def validate_password(cls, data: dict) -> bool:
        password1 = data['password']
        password2 = data['password2']
        standard = r'^(?=.*[a-z])(?=.*[A-Z]).+$'
        strong_password = True if len(password1) >= 8 and password1 == password2 and re.match(standard, password1) else False
        return strong_password
    
    @classmethod
    def redirect_client(cls, url: str) -> Type[redirect]:
        return redirect(url)
    
    @classmethod
    def validate_names(cls, request: HttpRequest) -> bool:
        data = cls.get_data(request)
        standard =  r'^[a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ]+$'
        names_is_valid = True if re.match(standard, data['first_name']) and re.match(standard, data['last_name'], ) else False
        return names_is_valid
    
    @classmethod
    def validate_email(cls, request: HttpRequest) -> bool:
        data = cls.get_data(request)
        standard = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        email_is_valid = True if re.match(standard, data['email']) else False
        return email_is_valid



        



                

