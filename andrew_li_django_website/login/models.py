from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    ''' UserProfile model which includes username and email '''

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    email = models.EmailField(max_length=70, default='')

    def __str__(self):
        ''' sends string representation of string back '''
        return self.user.username


def create_profile(sender, **kwargs):
    ''' when creating profile save user model '''
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
