from sites.project.models import Project, GithubConf


class ProjectService(object):
    def create_project(self, project_name, repo_obj):
        new_project = Project.objects.create(name=project_name, 
                                             github_repo=repo_obj)
        return new_project

    def create_github_conf(self, repo_uri, repo_name, repo_key=None):
        new_conf = GithubConf.objects.create(repo_uri=repo_uri,
                                             repo_name=repo_name,
                                             repo_key=repo_key)
        return new_conf

    def get_project_model(self):
        return Project

    def get_project_builds(self, project):
        return project.document_builds.all()

