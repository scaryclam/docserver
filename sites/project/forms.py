from django import forms


class ProjectForm(forms.Form):
    project_name = forms.CharField(max_length=255)
    repo_uri = forms.CharField(max_length=355)
    document_root = forms.CharField(max_length=100, required=False)

