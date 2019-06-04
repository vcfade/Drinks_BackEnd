
from django.contrib.redirects.middleware import RedirectallbackMiddleware

class CustomRedirectMiddleware():
  def process_response(self, request, response):
    pass