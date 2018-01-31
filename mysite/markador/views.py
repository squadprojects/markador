from django.shortcuts import render
from django.http import HttpResponse

def detail(request, bookmark_id):
    return HttpResponse("You're looking at bookmark %s." % bookmark_id)

