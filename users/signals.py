from django.db.models.signals import post_save, pre_delete
from .models import UserModel, UserDetailsModel
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=UserModel)
def create_details(sender, instance, created, **kwargs):
    if created:
        print("receiver signal..........")
        UserDetailsModel.objects.create(user=instance)

@receiver(post_save, sender=UserModel)
def save_details(sender, instance, **kwargs):
    instance.profile.save()
    print("instance...: ", instance)