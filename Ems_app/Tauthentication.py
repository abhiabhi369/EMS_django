from rest_framework.authentication import TokenAuthentication
from Ems_app.models import Token
from rest_framework import permissions


class TAuthentication(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            cookie_token = request.COOKIES['token_value']
            print('cookie_token',cookie_token)
            tokens = Token.objects.filter(token=cookie_token).values_list(flat=True)
            print('tokens',tokens[0])
            if tokens[0] == cookie_token:
                return True
            else:
                return False
        except:
            return False
