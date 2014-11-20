from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from datetime import datetime


def index(request):
    return HttpResponse('<html><body>Hello, World!</body></html>')


def about(request):
    return HttpResponse(
        "Nick is a pretty cool dude. Let's go back to <a href='/'>hello</a>"
    )


def better(request):
    t = loader.get_template('betterhello.html')
    c = Context({'current_time': datetime.now(), })
    return HttpResponse(t.render(c))