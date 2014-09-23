import requests


class GithubOAuthBackend(object):
    def authenticate(self, username=None, password=None):
        url = 'https://api.github.com/authorizations'

        resp = requests.post(url, auth=(username, password))
        two_factor_header = resp.headers.get("X-GitHub-OTP", False)
        if two_factor_header and two_factor_header.startswith("required"):
            # Oh no! This user has two factor auth turned on. Nevermind,
            # We'll add this into the session info and prompt the user
            # for a code that githib should be sending them
            import ipdb
            ipdb.set_trace()
 
