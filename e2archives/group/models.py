from django.db import models


class GroupPhotos(models.Model):
    image = models.ImageField(upload_to='group_images', null=True, blank=True, default=None)
