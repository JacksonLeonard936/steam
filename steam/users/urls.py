from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r"users",views.UserViewSet)
router.register(r"matches",views.MatchViewSet)
router.register(r"games",views.GameViewSet)
urlpatterns = [
    path("login", views.login, name="login"),
    path("scoreboard/", views.scoreboard,
     name="scoreboard")]
urlpatterns += router.urls