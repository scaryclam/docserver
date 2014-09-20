from django.conf.urls import patterns, include, url

from sites.project import views


urlpatterns = patterns('',
    url(r'^$', views.ProjectIndexView.as_view(), name='project-index'),
)

