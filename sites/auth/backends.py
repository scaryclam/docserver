import requests


class TwoFactorException(Exception):
    pass


class GithubOAuthBackend(object):
    def authenticate(self, username=None, password=None, auth_code=None):
        url = 'https://api.github.com/authorizations'

        headers = {}
        if auth_code:
            headers["X-GitHub-OTP"] = auth_code

        resp = requests.post(url, auth=(username, password))
        two_factor_header = resp.headers.get("X-GitHub-OTP", False)
        if two_factor_header and two_factor_header.startswith("required"):
            # Oh no! This user has two factor auth turned on. Nevermind,
            # We'll store this fact in the login view so that we know
            # to prompt them later. Raise rather than return.
            raise TwoFactorException
