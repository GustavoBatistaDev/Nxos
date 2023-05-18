from .models import UserCustom
from django.db.models.signals import post_save
from django.dispatch import receiver
from .active_account import ActiveAccount
from django.dispatch import receiver



@receiver(post_save, sender=UserCustom)
def active_account_mail(sender: UserCustom, instance: UserCustom, created, **kwargs):
    if created and not instance.is_active:
        active_account = ActiveAccount(instance)
        active_account.active_account_send_mail()


    
