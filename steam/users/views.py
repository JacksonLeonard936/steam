from django.shortcuts import render
from .models import User, Match, Game, SessionCookie
from rest_framework import viewsets
from .serializer import UserSerializer,MatchSerializer,GameSerializer,SessionCookieSerializer
import random, string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.decorators import api_view

def scoreboard(request):
    response = "<table>"
    response = f'{response} <tr>Game Name</tr> <tr>Winner Name</tr> <tr>Player Name</tr> <tr>Player Name</tr>'

    for match in Match.objects.all():
        response += "<tr>"
        response = f'{response} <td>{match.game.name}</td>'
        response = f'{response} <td>{match.winner.name}</td>'
        for player in match.players.all():
            response = f'{response} <td>{player.name}</td>'
        response += '</tr>'
    response = f'{response} </table>'
    return HttpResponse(response)

def index(request): 
    if User.objects.exists():
        user = User.objects.first()
        return HttpResponse(f'Hello {user.name}! This is your email: {user.email}')
    else:
        User.objects.create(name='Test', email='test@gmail.com', password='test')
    return HttpResponse("Hello, world. You're at the users index.")

@csrf_exempt
@api_view(["POST"])
def login(request):
    data = request.data
    email = data.get("email")
    password = data.get("password")
    user = None
    try:
        user = User.objects.get(email = email, password = password)
    except (User.DoesNotExist, User.MultipleObjectsReturned):
        return HttpResponse("Error finding user with email", status = 404)
    session_cookie_var = None
    try:
        session_cookie_var = SessionCookie.objects.get(account = user, is_active = True)
    except SessionCookie.DoesNotExist:
        session_cookie_var = SessionCookie.objects.create(account = user, cookie = "".join(random.choice(string.ascii_lowercase) for i in range(16)))
    return HttpResponse(session_cookie_var.cookie, status = 200)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer