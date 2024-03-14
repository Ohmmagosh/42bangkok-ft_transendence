from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pingpong/index.html', {})


def game(request, room_name):
    return render(request, 'pingpong/game.html', {'room_name': room_name})