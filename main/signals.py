from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Pi, Order


# @receiver(post_save, sender=Order) 
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Pi.objects.create(order=instance)
  
# @receiver(post_save, sender=Order) 
# def save_profile(sender, instance, **kwargs):
#     try:
#         instance.pi.save()
#     except Pi.DoesNotExist:
#         pass