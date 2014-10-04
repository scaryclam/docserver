from django import forms


class GithubLoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    two_factor_code = forms.CharField(max_length=50, required=False,
                                      widget=forms.HiddenInput)
