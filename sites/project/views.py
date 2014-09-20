from django.views.generic import ListView

from sites.project.services import ProjectService


class ProjectIndexView(ListView):
    model = ProjectService().get_project_model()
    template_name = 'project/project_index.html'

