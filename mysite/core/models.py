from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.urls import reverse


class Profile(models.Model):
	LANG = (
    ('Java', 'Java'),
    ('C', 'C'),
    ('Python', 'Python'),
	)
	Gender = (
    ('male', 'Male'),
    ('female', 'Female'),
   
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.TextField(choices=Gender,max_length=500, blank=True)
	language = models.CharField(choices= LANG,max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)

	def get_absolute_url(self):
	    return reverse('update', kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

