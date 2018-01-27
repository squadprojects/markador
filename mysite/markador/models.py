from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_public = models.BooleanField()
    date_created = models.DateTimeField('date created', auto_now_add=True,)
    date_updated = models.DateTimeField('date updated', null=True,auto_now_add=True)
    owner = models.ForeignKey(User, related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created']

    def __str__(self):
        return self.title
