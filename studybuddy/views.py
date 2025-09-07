from django.shortcuts import render

from .models import Room

# Create your views here.
# room_list = [
#     {'id':1, 'name':'Lets Learn Python!'},
#     {'id':2, 'name':'Design with me'},
#     {'id':3, 'name':'Frontend Developers'},
# ]

def home(request):
    room_list = Room.objects.all()
    context = {'rooms':room_list}
    return render (request, "home.html", context)

def rooms(request, pk):
    room = Room.objects.get(id=pk)
    context = {'rooms':room}
    return render(request, 'rooms.html', context)

def CreateRoom(request):
    return render(request, 'room_form.html')