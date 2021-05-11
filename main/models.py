from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from events.models import *
from registration.models import *
from records.models import *


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.course


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(blank=True, max_length=10)
    email = models.EmailField(max_length=150)
    mobile = models.CharField(max_length=10)
    course = models.ForeignKey(Courses, on_delete=models.PROTECT, null=True)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class GalleryFolder(models.Model):
    id = models.AutoField(primary_key=True)
    folder_name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Gallery Folder"

    def __str__(self):
        return self.folder_name


class ImageGallery(models.Model):
    img_id = models.AutoField(primary_key=True)
    image_name = models.CharField(blank=True, max_length=30)
    image = models.ImageField(upload_to='ImageGallery/')
    folder_id = models.ForeignKey(GalleryFolder, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Image Gallery"

    def __str__(self):
        return self.image_name

    @property
    def convert(self):
        myurl = str(self.image,'utf-8')
        return myurl


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    is_active = models.BooleanField(default=1)

    class Meta:
        verbose_name_plural = "Notice"
    
    def __str__(self):
        return self.content
