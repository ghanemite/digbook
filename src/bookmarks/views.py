from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import BookmarkSaveForm, RegistrationForm
from .models import Bookmark, Link, Tag


def main_page(request):
    context = {
        'head_title':'DigBookmarks',
    }
    return render(request,'bookmarks/main_page.html', context)


def user_page(request, username):
    user = get_object_or_404(User, username=username)
    bookmarks = user.bookmarks.order_by('-id')
    context = {
        'username':username,
        'bookmarks':bookmarks,
        'show_tags':True
    }
    return render(request,'bookmarks/user_page.html', context)


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


@login_required
def bookmark_save_page(request):
    if request.method == 'POST':
        form = BookmarkSaveForm(request.POST)
        if form.is_valid():
            # create or get link
            link, dummy = Link.objects.get_or_create(
                url = form.cleaned_data.get('url'),
            )

            # create or get bookmark
            bookmark, created = Bookmark.objects.get_or_create(
                user = request.user,
                link = link
            )

            # update bookmark title
            bookmark.title = form.cleaned_data.get('title')

            # if the bookmark is being updated clear the tag list
            if not created:
                bookmark.tags.clear()
            
            # create new tag list
            tag_names = form.cleaned_data.get('tags').split(',')
            for tag_name in tag_names:
                tag, dummy = Tag.objects.get_or_create(
                    name = tag_name
                )
                bookmark.tags.add(tag)
            
            # save teh bookmark to the database
            bookmark.save()

            return HttpResponseRedirect('/user/{username}'.format(
                username = request.user.username
            ))
    else:
        form = BookmarkSaveForm()
    return render(request, 'bookmarks/bookmark_save.html', {'form':form})


def tag_page(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    bookmarks = tag.bookmarks.order_by('-id')
    context = {
        'bookmarks': bookmarks,
        'tag': tag,
        'show_tags': True,
        'show_user': True
    }
    return render(request,'bookmarks/tag_page.html', context)
