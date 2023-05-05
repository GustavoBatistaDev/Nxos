from django.http import HttpRequest


class DataClient:

  
    @classmethod
    def get_data(cls, request: HttpRequest, **kwargs):
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
        for i in data.values():
            match i:
                case '':
                    return False
                case _:
                    continue
        return data 
    

    @classmethod
    def validate_password(cls, data: dict):
        password1 = data['password']
        password2 = data['password2']
        strong_password = True if len(password1) >= 8 and password1 == password2 else False
        return strong_password
        



                

