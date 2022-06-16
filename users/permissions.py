from rest_framework import permissions
from .models import User, SessionCookie

class HasSessionTokenPermission(permissions.BasePermission):
    def has_permission(self, request, view):   
        user_id = request.query_params["user"]
        user = User.objects.get(id = user_id)
        session_cookie = request.query_params["session_cookie"]
        is_valid_cookie = SessionCookie.objects.filter(is_active = True, account = user_id, cookie = session_cookie).exists()
        return is_valid_cookie
