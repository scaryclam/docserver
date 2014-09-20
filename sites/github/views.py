from django.views.generic import View
from django.http import HttpResponse

from sites.github.services import GithubService
from sites.docbuilder.services import DocBuilderService


class WebhookView(View):
    def post(self, request, *args, **kwargs):
        payload_data = GithubService().process_webhook_payload()
        DocBuilderService().trigger_build()
        
        return HttpResponse("Hello Github")

