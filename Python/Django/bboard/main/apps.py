from django.apps import AppConfig
from django.dispatch import Signal
from .utilities import send_activation_notification, send_new_comment_notification
from django.db.models.signals import post_save

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Доска объявлений'

def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])
