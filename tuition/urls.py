from django.contrib import admin
from django.urls import path

from .views import ContactView, PostDetailView, PostListView, postview, subjectview,PostCreateView
from .forms import ContactFormtwo
# app_name='tuition'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact2/', ContactView.as_view(form_class=ContactFormtwo,template_name="contact2.html"), name='contact'),

    path('post/', postview, name="postview"),
    path('postlist/',PostListView.as_view(),name="postlist"),
    path('postdetail/<int:pk>/',PostDetailView.as_view(),name="postdetails"),

    
    # path('postcreate/', postcreate, name='postcreate'),
    path('postcreate/', PostCreateView.as_view(), name='postcreate'),
    path('subject/', subjectview, name='subject'),
]
