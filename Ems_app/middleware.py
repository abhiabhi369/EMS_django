from django.utils.deprecation import MiddlewareMixin
from Ems_app.models import Token,Users

class CustomAuthMiddleware(MiddlewareMixin):
    print('hello................')
    def process_request(self, request):
        try:
            cookie_token = request.COOKIES['token_value']
            # print('cookie_token',cookie_token)
            user = Token.objects.filter(token=cookie_token).values_list('user',flat=True)
            # print('user1',user)
            if user:
                print('in middleware if')
                master_user = Users.objects.get(email=user[0])
                # print('master_user',master_user)
                request.user1 = master_user
            else:
                request.user1 = 'AnonymousUser'
        except:
            print('in except')
            request.user1 = 'AnonymousUser'
