import re
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse

EXEMPT_URLS = []
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
    def __init__ (self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response   

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        print(path)


        if not any(url.match(path) for url in EXEMPT_URLS):
            if not request.user.is_authenticated:
            
                #return Response ({"detail": "NOT AUTHENTICATED"}, status=status.HTTP_401_UNAUTHORIZED)
                return JsonResponse({'error': 'Some error'}, status=401)