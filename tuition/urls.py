from django.contrib import admin
from django.urls import path

from .views import ContactView, postcreate, postview, subjectview
from .forms import ContactFormtwo

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact2/', ContactView.as_view(form_class=ContactFormtwo,template_name="contact2.html"), name='contact'),

    path('post/', postview, name="postview"),
    path('postcreate/', postcreate, name='postcreate'),
    path('subject/', subjectview, name='subject'),
]
