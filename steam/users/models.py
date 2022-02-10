from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    email = models.EmailField()

class Game(models.Model):
    name = models.CharField(max_length=25)

class Match(models.Model):
    players = models.ManyToManyField(to=User)
    winner = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name="Winning_matches")
    game = models.ForeignKey(to=Game, on_delete=models.PROTECT)

class SessionCookie(models.Model):
    account = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name="session_cookies")
    cookie = models.CharField(unique=True, max_length=16)
    created_at = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=True)