from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    url = models.URLField()


class Bookmark(models.Model):
    user = models.ForeignKey(User, related_name='bookmarks')
    link = models.ForeignKey(Link, related_name='link')
    title = models.CharField(max_length=200)

