import os

from django.conf import settings

from sites.project.models import Project, GithubConf


class ProjectService(object):
    def create_project(self, project_name, repo_obj):
        new_project = Project.objects.create(name=project_name,
                                             github_conf=repo_obj)
        return new_project

    def create_github_conf(self, repo_uri, document_root='docs', repo_key=None):
        repo_owner, repo_name = repo_uri.split('/')
        new_conf = GithubConf.objects.create(repo_uri=repo_uri,
                                             repo_owner=repo_owner,
                                             repo_name=repo_name,
                                             repo_key=repo_key,
                                             document_root=document_root)
        return new_conf

    def get_project_model(self):
        return Project

    def get_project_builds(self, project):
        return project.document_builds.all()

    def get_project_by_owner_and_name(self, repo_owner, repo_name):
        project = Project.objects.get(github_conf__repo_owner=repo_owner,
                                      github_conf__repo_name=repo_name)
        return project

    def get_document_from_path(self, project, path):
        docs_base = os.path.join(project.github_conf.repo_owner,
                                 project.github_conf.repo_name)
        doc_root = project.github_conf.document_root
        document_path = os.path.join(docs_base, doc_root, '_build/html/', path)
        return document_path
