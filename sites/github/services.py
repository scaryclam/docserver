from github2.client import Github


class GithubService(object):
    def _get_client(self, username, api_token):
        return Github(username=username, api_token=api_token)

    def process_webhook_payload(self):
        pass

    def clone_repo(self, repo_url):
        pass

    def update_repo(self, repo_url, branch):
        pass

    def login_user(self, username):
        pass
