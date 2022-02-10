from rest_framework import serializers
from .models import User,Match,Game,SessionCookie
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class SessionCookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionCookie
        fields = "__all__"