# signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import logging

logger = logging.getLogger(__name__)

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     logger.debug(f'create_profile for {sender}')
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     logger.debug(f'save_profile for {sender}')
#     instance.profile.save()