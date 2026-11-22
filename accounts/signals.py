from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile
from mymovie import settings
from django.contrib.auth.models import Group

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        members_group = Group.objects.get(name='Members')
        members_group.user_set.add(instance)
        Profile.objects.create(pk=instance.pk,)
        send_mail(
            subject='Profile Created',
            message=f'Profile {instance.pk} has been created',
            from_email=settings.COMPANY_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )