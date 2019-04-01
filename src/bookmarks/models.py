from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class Bookmark(models.Model):
    user = models.ForeignKey(User, related_name='bookmarks')
    link = models.ForeignKey(Link, related_name='link')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title



class Tag(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    bookmarks = models.ManyToManyField(Bookmark, related_name='tags')

    def __str__(self):
        return self.name
