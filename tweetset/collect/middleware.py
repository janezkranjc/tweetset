from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social.exceptions import SocialAuthBaseException
from django.conf import settings
from django.contrib.messages.api import MessageFailure
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.http import urlquote

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if isinstance(exception, SocialAuthBaseException):
            backend_name = request.backend.name
            message = self.get_message(request, exception)
            url = self.get_redirect_uri(request, exception)
            try:
                messages.error(request, message)
            except MessageFailure:
                url += ('?' in url and '&' or '?') + \
                       'message={0}&backend={1}'.format(urlquote(message),
                                                        backend_name)
            return redirect(url)
