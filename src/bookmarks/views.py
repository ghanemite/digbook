from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


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