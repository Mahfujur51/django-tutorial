from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import HomeView, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='homeview'),
    path('home/', home, name='home'),
    path('tuition/', include('tuition.urls')),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
