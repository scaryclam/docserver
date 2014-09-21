from django.views.generic import ListView, View, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from sites.project.services import ProjectService
from sites.project.forms import ProjectForm
from sites.docbuilder.services import DocBuilderService


class ProjectIndexView(ListView):
    model = ProjectService().get_project_model()
    template_name = 'project/project_index.html'


class ProjectView(View):
    def get(self, request, *args, **kwargs):
        project = ProjectService().get_project_by_owner_and_name(kwargs['repo_owner'],
                                                                 kwargs['repo_name'])
        return HttpResponse("This is a project")


class ProjectCreateView(FormView):
    form_class = ProjectForm
    template_name = 'project/project_create.html'

    def form_valid(self, form, *args, **kwargs):
        project_service = ProjectService()
        docbuilder_service = DocBuilderService()
        repo_obj = project_service.create_github_conf(
            form.cleaned_data['repo_uri'])
        new_project = project_service.create_project(
            form.cleaned_data['project_name'], repo_obj)
        docbuilder_service.create_doc_structure(new_project)
        docbuilder_service.trigger_build(new_project)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('project-index')

