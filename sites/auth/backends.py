import json
import requests

from django.contrib.auth.models import User


class TwoFactorException(Exception):
    pass


class GithubOAuthBackend(object):
    """ This backend will attempt to log into github using the given username
        and password. If successful it will then get or create the
    """
    def authenticate(self, username=None, password=None, auth_code=None):
        url = 'https://api.github.com/authorizations'

        try:
            # Attempt to get an existing user
            user = User.objects.get(username=username)
            user_is_authenticated = user.check_password(password)
        except User.DoesNotExist:
            # No such user. Don't do anything else
            return

        # Now check with github. If the existing token is still valid, then
        # the user can be logged in. Otherwise, try and get a new one.
        # If there is no token, try and get a new one.
        # If checking / setting the token fails, we don't authenticate the user.
        if user.oauth_token:
            self.check_github_token(user, username, password, auth_code)
        else:
            self.create_token(user, username, password, auth_code)

    def check_github_token(self):
        resp = requests.get(url='https://api.github.com/user',
                            auth=(user.oauth_token, 'x-oauth-basic'))
        if resp.status_code != 201:
            return False
        return True

    def create_token(self, user, username, password, auth_code=None):
        headers = {}
        payload = {
            'note': 'Docserver',
            'scopes': [
                'public_repo'
            ]
        }
        if auth_code:
            headers["X-GitHub-OTP"] = auth_code
        resp = requests.post(url,
                             auth=(username, password),
                             headers=headers,
                             data=json.dumps(payload))
        two_factor_header = resp.headers.get("X-GitHub-OTP", False)
        if two_factor_header and two_factor_header.startswith("required"):
            # Oh no! This user has two factor auth turned on. Nevermind,
            # We'll store this fact in the login view so that we know
            # to prompt them later. Raise rather than return.
            raise TwoFactorException
