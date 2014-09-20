from django.views.generic import View
from django.http import HttpResponse

from sites.github.services import GithubService


class WebhookView(View):
    def post(self, request, *args, **kwargs):
        GithubService().process_webhook_payload()
        return HttpResponse("Hello Github")

