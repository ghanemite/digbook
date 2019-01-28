from django.contrib import admin

from .models import Bookmark, Link


admin.site.register(Bookmark)
admin.site.register(Link)
