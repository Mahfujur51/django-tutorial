from django.contrib import admin
from django.urls import path

from .views import contact, postview, postcreate, subjectview

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('post/', postview, name="postview"),
    path('postcreate/', postcreate, name='postcreate'),
    path('subject/', subjectview, name='subject'),
]
