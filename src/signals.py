
from django.db.models.signals import post_save
from django.dispatch import receiver
from genz.models import Profile
from django.contrib.auth.models import User
from archive.models import Archive




@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        archive = Archive.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def create_archive(sender, instance, created, *args, **kwargs):
#     if created:
#         archive = Archive.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, *args, **kwargs):
#     if not created:
#         profile = instance.profile
#         username = instance.username
#         profile.code = username
#         profile.save()
#         print('profile updated!')
