from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from sites.user.forms import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('project-index')

