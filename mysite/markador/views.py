from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Bookmark


def bookmark_user(request, username):
    return HttpResponse("You're looking at the view for user %s" % username)


def bookmark_list(request):
    bookmarks = Bookmark.is_public
    context = {'bookmarks': bookmarks}
    return render(request, 'marcador/bookmark_list.html', context)


def detail(request, bookmark_id):
    return HttpResponse("You're looking at bookmark %s." % bookmark_id)
