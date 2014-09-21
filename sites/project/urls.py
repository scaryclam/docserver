from django.conf.urls import patterns, include, url

from sites.project import views


urlpatterns = patterns('',
    url(r'^$', views.ProjectIndexView.as_view(), name='project-index'),
    url(r'(?P<repo_owner>.*)/(?P<repo_name>.*)', views.ProjectView.as_view(), name="project"),
    url(r'^create', views.ProjectCreateView.as_view(), name="project-create"),
)

