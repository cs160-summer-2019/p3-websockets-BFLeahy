from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})
  
def display(request):
    return render(request, 'draw/display.html', {})
  
def variation(request):
    return render(request, 'draw/variation.html', {})

"""def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
    """