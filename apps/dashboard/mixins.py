from django.http import HttpRequest, HttpResponse
from authentication.mixins import ValidatorMixin
import re


class ValidatorProfileMixin(ValidatorMixin):

    @classmethod
    def get_data(cls, request: HttpRequest, **kwargs) -> dict:
        data = {}
        fullname = request.POST.get('fullname' or '')
        photo = request.FILES.get('photo' or '')
        email = request.POST.get('email' or '')
        mobile = request.POST.get('mobile' or '')
        address = request.POST.get('address' or '')
        data['fullname'] = fullname
        data['photo'] = photo
        data['email'] = email
        data['mobile'] = mobile
        data['address'] = address
        return data
    

    @classmethod
    def validate_fullname(cls, request):
        data = cls.get_data(request)
        standard = r'^[a-zA-ZÀ-ÿ\s]+$'
        return True if re.match(standard, data['fullname']) else False
    
    @classmethod
    def validate_mobile(cls, request):
        data = cls.get_data(request)
        standard = r'^\d+$'
        return True if re.match(standard, data['mobile']) else False

    @classmethod
    def validate_address(cls, request):
        data = cls.get_data(request)
        standard = r'^(?=.*[a-z])(?=.*[A-Z]).+$'
        return True if re.match(standard, data['address']) else False
    
    