from django.shortcuts import render
from .models import Profile


def index(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'member_profile.html', context)


def profile(request, id):
    profiles = Profile.objects.get(id=id)
    context = {
        'profiles': profiles
    }
    return render(request, 'profile.html', context)
