from django.contrib.auth.models import AnonymousUser
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from users.models import UserToken


class TokenAuthentication(BaseAuthentication):
    def __init__(self):
        self.keyword = 'Token'
        self.raise_exception = True

    # def __call__(self, request):
    #     auth = str(request.META.get('HTTP_AUTHORIZATION', ''))
    #     if auth != '' and str(auth) != "Token undefined":
    #         user, token = self.authenticate(request)

    def authenticate(self, request):
        # Authorization header is in the format request.META.get('HTTP_AUTHORIZATION', b'')
        auth = get_authorization_header(request).split()

        # if auth token was provided in header, we proceed with it
        if auth and auth[0].lower() == self.keyword.lower().encode():
            if len(auth) == 1:
                msg = 'Invalid token header. No credentials provided.'
                raise exceptions.AuthenticationFailed(msg)
            elif len(auth) > 2:
                msg = 'Invalid token header. Token string should not contain spaces.'
                raise exceptions.AuthenticationFailed(msg)

            try:
                token = auth[1].decode()
            except UnicodeError:
                msg = 'Invalid token header. Token string should not contain invalid characters.'
                raise exceptions.AuthenticationFailed(msg)
        # if no tokens were provided, we return nothing
        else:
            return AnonymousUser(), None
        # if everything was okay, we authenticate the user
        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        try:
            token = UserToken.objects.get(key=key)
        except UserToken.DoesNotExist:
            if self.raise_exception:
                raise exceptions.AuthenticationFailed('Token is no longer valid.')
            else:
                return AnonymousUser(), None

        if not token.validate():
            return AnonymousUser(), None
        token.renew()
        return token.user, None

    def authenticate_header(self, request):
        """
        Needed for BaseAuthentication overriding
        """
        return self.keyword
