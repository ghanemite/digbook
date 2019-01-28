from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def main_page(request):
    context = {
        'head_title':'DigBookmarks',
        'page_title':'Welcome to Django Bookmarks',
        'page_body':'Where you can store your bookmarked links',
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
