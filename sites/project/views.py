from django.views.generic import ListView, View, FormView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.response import SimpleTemplateResponse
from django.core.urlresolvers import reverse

from sites.project.services import ProjectService
from sites.project.forms import ProjectForm
from sites.docbuilder.services import DocBuilderService
from sites.github.services import GithubService


class ProjectIndexView(ListView):
    model = ProjectService().get_project_model()
    template_name = 'project/project_index.html'

    def get_context_data(self):
        context = super(ProjectIndexView, self).get_context_data()
        return context


class ProjectView(View):
    def get(self, request, *args, **kwargs):
        project = ProjectService().get_project_by_owner_and_name(
            kwargs['repo_owner'], kwargs['repo_name'])
        return HttpResponse("This is a project config page!")


class ProjectDocsView(View):
    def get(self, request, *args, **kwargs):
        service = ProjectService()
        project = service.get_project_by_owner_and_name(kwargs['repo_owner'],
                                                        kwargs['repo_name'])
        document = service.get_document_from_path(project, kwargs['path'])
        if document is None:
            raise Http404

        return SimpleTemplateResponse(document)


class ProjectCreateView(View):
    template_name = 'project/project_create.html'

    def post(self, request, *args, **kwargs):
        project_service = ProjectService()
        docbuilder_service = DocBuilderService()
        import ipdb
        ipdb.set_trace()
        repo_obj = project_service.create_github_conf(
            form.cleaned_data['repo_uri'])
        new_project = project_service.create_project(
            form.cleaned_data['project_name'], repo_obj)
        docbuilder_service.create_doc_structure(new_project)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('project-index')


class RepositoriesListView(ListView):
    model = ProjectService().get_project_model()
    template_name = 'project/repo_list.html'

    def get_context_data(self):
        context = super(RepositoriesListView, self).get_context_data()
        service = GithubService()

        user_repos = service.get_user_repos(self.request.user)
        org_repos = service.get_org_repos(self.request.user)

        context['user_repos'] = user_repos
        context['org_repos'] = org_repos
        for repo in org_repos:
            project = self.model.objects.filter(github_conf__repo_name=repo['full_name'])
            if project:
                context['org_repos'].pop(repo['full_name'])
        return context
