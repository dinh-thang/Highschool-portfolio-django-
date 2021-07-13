from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    information = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='profile_images')
