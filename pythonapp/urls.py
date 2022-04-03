from django.contrib import admin
from django.urls import include, path

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('tuition/',include('tuition.urls')),

]