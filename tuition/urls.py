from django.contrib import admin
from django.urls import path

from .views import contact, postview, postcreate

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('post/', postview, name="postview"),
    path('postcreate/', postcreate, name='postcreate')
]
