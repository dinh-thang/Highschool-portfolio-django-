from django.shortcuts import render
from .models import GroupPhotos


def index(request):
    group_photos = GroupPhotos.objects.all()
    context = {
        'group_photos': group_photos
    }
    return render(request, 'group.html', context)
