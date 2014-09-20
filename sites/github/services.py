from github2.client import Github


class GithubClientService(object):
    def _get_client(self, username, api_token):
        return Github(username=username, api_token=api_token)

    def process_webhook_payload(self):
        pass

