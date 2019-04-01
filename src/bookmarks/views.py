from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import BookmarkSaveForm, RegistrationForm, SearchForm
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


def tag_cloud_page(request):
    MAX_WEIGHT = 5
    tags = Tag.objects.all().order_by('name')

    # calculating tag, min and max count.
    min_count = max_count = tags[0].bookmarks.count()
    for tag in tags:
        tag.count = tag.bookmarks.count()
        if tag.count < min_count:
            min_count = tag.count
        if max_count < tag.count:
            max_count = tag.count
        
    # calculate count range. and we avoid dividing by zero.
    range = float(max_count - min_count)
    if range == 0.0:
        range = 1.0
    
    # calculate tag weights
    for tag in tags:
        tag.weight = int(
            MAX_WEIGHT*(tag.count - min_count) / range
        )

    return render(request, 'bookmarks/tag_cloud_page.html', {'tags':tags})



def search_page(request):
    form = SearchForm()
    bookmarks = []
    show_results = False
    if 'query' in request.GET:
        show_results = True 
        query = request.GET['query'].strip()
        if query:
            form = SearchForm({'query': query})
            bookmarks = Bookmark.objects.filter(
                title__icontains=query)[:10]
    
    context = {
        'form':form,
        'bookmarks':bookmarks,
        'show_results':show_results,
        'show_tags':True,
        'show_user': True
    }

    if 'ajax' in request.GET:
        return render(request, 'bookmarks/bookmark_list.html', context)
    else:
        return render(request, 'bookmarks/search.html', context)