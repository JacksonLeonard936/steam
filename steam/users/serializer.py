from rest_framework import serializers
from .models import User,Match,Game,SessionCookie
class UserSerializer(serializers.ModelSerializer):
    matches_played = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        #TODO: remove password from serializer
        fields = "__all__"
    def get_matches_played(self, obj):
        return Match.objects.filter(players__in = [obj]).count()

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