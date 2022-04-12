import email
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import SignupForm, UserProfileForm
from .models import Profile

# Create your views here.


def loginuser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homeview')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'session/login.html', {'form': form})


def logoutuser(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('homeview')


def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            mail_subject = "An Account Created"
            message = render_to_string('session/account.html', {
                'user': user,
                'domain': current_site.domain
            })
            send_mail = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[send_mail])
            email.send()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 'Account created for please Check usermail ' + username)
            return redirect('session:loginuser')
    else:
        form = SignupForm()
    return render(request, 'session/register.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Successfully Change!!")
            return redirect('homeveiw')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'session/change_pass.html', {'form': form})


def userProfile(request):
    try:
        instance = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        instance = None
    if request.method == 'POST':
        if instance:
            form = UserProfileForm(
                request.POST, request.FILES, instance=instance)
        else:
            form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Your Profile Save Successfully!!')
            return redirect('homeview')
    else:
        form = UserProfileForm(instance=instance)

    context = {
        'form': form
    }
    return render(request, 'session/updateprofile.html', context)

def ownerprofile(request):
    user = request.user
    return render(request,'session/userprofile.html',{'user':user})