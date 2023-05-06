from .models import UserCustom
from django.db.models.signals import post_save
from django.dispatch import receiver
from .active_account import ActiveAccount



#posso salvar algo no banco de dados pela propia funcao de sinal
# ex: quando um dado 'e salvo, posso salvar algo a mais a parir do sender
@receiver(post_save, sender=UserCustom)
def active_account_mail(sender: UserCustom, instance: UserCustom, created, **kwargs):
    if created and not instance.is_active:
        active_account = ActiveAccount(instance)
        active_account.active_account_send_mail()