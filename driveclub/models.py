from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
# Create your models here.


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}'


class Vehicle(models.Model):

    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, null=True, blank=True, related_name='vehicles')
    name = models.CharField(max_length=100)
    speed = models.PositiveIntegerField('bhp', null=True, blank=True)
    weight = models.PositiveIntegerField('kg', null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


# auto deletes files from media folder tied to the user
@receiver(pre_delete, sender=Vehicle)
def my_model_delete(sender, instance, **kwargs):
    instance.image.delete(False)
    instance.video.delete(False)
