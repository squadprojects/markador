from django.shortcuts import render
from django.http import HttpResponse

from .models import Bookmark

def bookmark_user(request, username):
    return HttpResponse("You're looking at the view for user %s" % username)

def bookmark_list(request):
    # bookmarks = Bookmark
    return HttpResponse("You're looking at the view for bookmark list")
    

def detail(request, bookmark_id):
    return HttpResponse("You're looking at bookmark %s." % bookmark_id)


