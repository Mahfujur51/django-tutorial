
from unicodedata import name
from django.urls import path

from .views import change_password, loginuser, logoutuser, ownerprofile, registration, userProfile
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = "session"
urlpatterns = [
    path('login/', loginuser, name='loginuser'),
    path('logout/', logoutuser, name='logoutuser'),
    path('registration/', registration, name='registration'),
    path('changepassword/', change_password, name='chagnepassword'),
    path('reset/password/', PasswordResetView.as_view(
        template_name='session/resetpassword.html'), name="password_reset"),
    path('reset/password/done', PasswordResetDoneView.as_view(
        template_name='session/resetpassworddone.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='session/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='session/password_reset_complete.html'), name="password_reset_complete"),
    path('userprofile/', userProfile, name='userprofile'),
    path('ownerprofile/', ownerprofile, name='ownerprofile')
]
