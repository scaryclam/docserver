import os
from sphinx.quickstart import generate

from django.conf import settings


class DocBuilderService(object):
    def trigger_build(self, project_settings):
        generate(project_settings)

    def get_project_settings(self, project):
        project_settings = {
            'path': doc_build_dir,
            'version': '0.1',
            'project': project.name,
            'author': '',
            'release': '0.1',
            'master': 'index',
            'sep': False,
            'dot': '_',
            'suffix': '.rst',
            'language': 'en',
            'epub': False,
            'ext_autodoc': False,
            'ext_doctest': False,
            'ext_intersphinx': False,
            'ext_todo': False,
            'ext_coverage': False,
            'ext_pngmath': False,
            'ext_mathjax': False,
            'ext_ifconfig': False,
            'ext_viewcode': False,
            'makefile': False,
            'batchfile': False,
        }
        return project_settings

    def create_doc_structure(self, project):
        """ Creates a new document config, if
            it's missing. We shouldn't overwrite the users
            config if they pre-made one.
        """
        base_git_dir = settings.GIT_CLONE_DIR
        doc_build_dir = os.path.join(
            base_git_dir, 
            project.github_conf.repo_owner,
            project.github_conf.repo_name,
            project.github_conf.document_root)
        if os.path.exists(os.path.join(base_git_dir, 'conf.py')):
            return
        print "Creating"
        project_settings = self.get_project_settings(project)
        self.trigger_build(project_settings)

