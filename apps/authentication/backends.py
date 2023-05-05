from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q
from django.http import HttpRequest

class CustomBackend(ModelBackend):
    def authenticate(self, request:HttpRequest, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.filter(
                Q(email__iexact=username)
            )
        except UserModel.DoesNotExist:
            return
        if user.exists():
            my_user = user.first()
            if my_user.check_password(password):
                return my_user
            return 
        else:
            return