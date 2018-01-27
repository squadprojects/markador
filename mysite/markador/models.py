from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model)
    url = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_public = models.BooleanField()
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    owner = models.ForeignKey(User, related_name='bookmarks')
    tags = models.ManytoManyField(Tag, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_pluarl = 'tags'
        ordering = ['name']

    def __str__(self):
        return self.name
