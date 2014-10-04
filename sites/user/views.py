from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from sites.user.forms import GithubLoginForm


class LoginView(FormView):
    form_class = GithubLoginForm
    template_name = 'user/login.html'

    def form_valid(self, form):
        # Try and log the user in
        try:
            user = User.objects.get(username=form.cleaned_data['username'])
        except User.DoesNotExist:
            raise
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('project-index')
