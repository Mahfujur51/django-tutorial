
from django.urls import path

from .views import loginuser, logoutuser, registration

app_name="session"
urlpatterns = [
    path('login/',loginuser,name='loginuser'),
    path('logout/',logoutuser,name='logoutuser'),
    path('registration/',registration,name='registration'),
]
