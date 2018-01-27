from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model)
    url = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_public = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, 'date created')
    date_updated = models.DateTimeField(null=True,auto_now_add=True, 'date updated')
    owner = models.ForeignKey(User, related_name='bookmarks')
    tags = models.ManytoManyField(Tag, blank=True)

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created']

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_pluarl = 'tags'
        ordering = ['name']

    def __str__(self):
        return self.name
