from os import replace
from django.shortcuts import render
from .models import User, Match, Game, SessionCookie
from rest_framework import viewsets
from .serializer import UserSerializer,MatchSerializer,GameSerializer,SessionCookieSerializer
import random, string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .permissions import HasSessionTokenPermission
import json
from rest_framework.response import Response

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
    return_info = {}
    return_info["session_token"] = session_cookie_var.cookie
    return_info["user_id"] = user.id
    return HttpResponse(json.dumps(return_info), status = 200)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    # Know the id of user creating game, ask user for email of opponent
    def retrieve(self, request, pk):
        print(request.GET.get("user_id"))
        user_id = request.GET.get("user_id")
        user = User.objects.get(id = user_id)
        instance = self.get_object()
        if user not in instance.players.all():
            return HttpResponse(status = 401)
        return Response(MatchSerializer(instance).data)



    def create(self, request):
        data = request.data
        creator_id = data.get("creator_id")
        game_name = data.get("game_name")
        opponent_email = data.get("opponent_email")
        creator = User.objects.get(id = creator_id)
        game = Game.objects.get(name = game_name)
        opponent = User.objects.get(email = opponent_email)
        match = Match.objects.create(game = game)
        match.players.set([creator, opponent])
        match.save()
        return Response(MatchSerializer(match).data)

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer