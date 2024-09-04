from django.contrib.auth.models import User
from blogapp.models import Blog
from django.core.mail import send_mail
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete


@receiver(post_save, sender=Blog)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        # subject = 'Welcome to our site!'
        # message = f'Hi {instance.username}, thank you for registering at our site.'
        # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])
        print("send function is called ")

@receiver(pre_save, sender=Blog)
def before_save(sender, instance, *args, **kwargs):
    print("object created before function is called")


@receiver(pre_delete, sender=Blog)
def before_delete(sender, instance, *args, **kwargs):
    print("object deleted before function is called")

@receiver(post_delete, sender=Blog)
def post_delete(sender, instance, *args, **kwargs):
    print("object deleted post function is called")