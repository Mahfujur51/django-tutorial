from django.contrib import admin
from django.urls import path

from .forms import ContactFormtwo
from .views import (ContactView, PostCreateView, PostDetailView, PostListView,
                    PostUpdateView, contact,filter, postview, search, subjectview,PostDeleteView)

app_name='tuition'

urlpatterns = [
    # path('contact/',contact,name='contact'),
    path('contact/', ContactView.as_view(), name='contact'),
    # path('contact2/', ContactView.as_view(form_class=ContactFormtwo,template_name="contact2.html"), name='contact'),

    path('post/', postview, name="postview"),
    path('postlist/', PostListView.as_view(), name="postlist"),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name="postdetails"),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name="edit"),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name="delete"),
    path('search/', search, name="search"),
    path('filter/',filter,name="filter"),



    # path('postcreate/', postcreate, name='postcreate'),
    path('postcreate/', PostCreateView.as_view(), name='postcreate'),
    path('subject/', subjectview, name='subject'),
]
