from .models import UserCustom
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import os 


class ActiveAccount:
    def __init__(self, user: UserCustom) -> None:
        if not isinstance(user, UserCustom):
            raise ValueError('user needs to be an instance of Users')

        self._user = user
    
    def _generate_url(self):
        protocol = 'http' 
        domain = settings.DOMAIN
        uid = urlsafe_base64_encode(force_bytes(self._user.pk))
        token = default_token_generator.make_token(self._user)

        print(f"{protocol}://{domain}{reverse('active_account', kwargs={'uidb4': uid, 'token':token})}")
        return f"{protocol}://{domain}{reverse('active_account', kwargs={'uidb4': uid, 'token':token})}"

    def active_account_send_mail(self):
        active_url = self._generate_url()
        subject = 'Hello, Friend! Active your account now.' 

        path_templates_email = os.path.join(settings.BASE_DIR, 'apps/authentication/templates/emails/active_account.html')
        email_body = render_to_string(path_templates_email, {'active_url':active_url})
        email = EmailMessage(subject, email_body, to=[self._user.email])
        email.send()


