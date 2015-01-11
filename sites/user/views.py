from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model, login, authenticate

from sites.user.forms import GithubLoginForm, RegisterForm
from sites.auth.backends import TwoFactorException


User = get_user_model()


class LoginView(FormView):
    form_class = GithubLoginForm
    template_name = 'user/login.html'

    def form_valid(self, form):
        # Try and log the user in
        try:
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                auth_code=form.cleaned_data.get('two_factor_code', None))
        except TwoFactorException:
            form.errors['two_factor'] = 'Code Required'
            return self.form_invalid(form)
        except Exception, err:
            raise

        if user and user.is_active:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('project-index')


class RegisterView(LoginView):
    """ This extends the LoginView as we would like to log the user in upon
        signup.
    """
    form_class = RegisterForm
    template_name = 'user/register.html'

    def form_valid(self, form):
        try:
            User.objects.create(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
        except Exception, err:
            import ipdb
            ipdb.set_trace()
            raise
        super(RegisterView, self).form_valid(form)

    def get_success_url(self):
        return reverse('user-login')
