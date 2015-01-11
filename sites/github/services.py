import json
import requests
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

    def get_user_repos(self, user):
        url = 'https://api.github.com/users/%s/repos?per_page=500' % user.github_username
        resp = requests.get(url=url, auth=(user.oauth_token, 'x-oauth-basic'))
        content = json.loads(resp.content)
        return content

    def _get_single_org_repos(self, user, org):
        url = "%s?per_page=500" % org['repos_url']
        resp = requests.get(url=url, auth=(user.oauth_token, 'x-oauth-basic'))
        return json.loads(resp.content)

    def get_org_repos(self, user):
        org_repos = []
        orgs = self.get_user_orgs(user)

        for org in orgs:
            repos = self._get_single_org_repos(user, org)
            org_repos.extend(repos)
        return org_repos

    def get_user_orgs(self, user):
        resp = requests.get(
            url="https://api.github.com/users/%s/orgs" % user.github_username,
            auth=(user.oauth_token, 'x-oauth-basic'))
        content = json.loads(resp.content)
        return content
