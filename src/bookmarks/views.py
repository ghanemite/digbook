from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView

from .forms import RegistrationForm


def main_page(request):
    context = {
        'head_title':'DigBookmarks',
    }
    return render(request,'main_page.html', context)


def user_page(request, username):
    user = get_object_or_404(User, username=username)
    bookmarks = user.bookmarks.all()
    context = {
        'username':username,
        'bookmarks':bookmarks,
    }
    return render(request,'user_page.html', context)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            email    = form.cleaned_data.get('email')
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email
            )
            messages.success(request, '''Your accounted created successfully\n
            Pleaese Log in .''')
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    return render(request,'registration/signup.html', {'form':form})


    
