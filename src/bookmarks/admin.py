from django.contrib import admin

from .models import Bookmark, Link, Tag


admin.site.register(Bookmark)
admin.site.register(Link)
admin.site.register(Tag)

