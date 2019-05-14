from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import Http404
import json


def index(request):
    return render(request, 'chatting/index.html', {})

def room(request, room_name):
    username = request.GET.get('user',None)
    if username and User.objects.filter(username=username).exists():
        return render(request, 'chatting/room_new.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(username)),
        })
    raise Http404("Chat does not exist")
