from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import logout


class HomeView(TemplateView):
    template_name = "home.html"


class LogoutView(RedirectView):
    url = '/'
    permanent = False

    def get(self, request, *args, **kwargs):
        logout(request)
        response = super(LogoutView, self).get(request, *args, **kwargs)
        return response
