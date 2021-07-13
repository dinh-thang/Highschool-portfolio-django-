from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='member'),
    path('/<int:id>', views.profile, name='profile')
]