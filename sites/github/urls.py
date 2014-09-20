from django.conf.urls import patterns, include, url

from sites.github import views


urlpatterns = patterns('',
    url(r'^$', views.WebhookView.as_view(), name='webhook-reciever'),
)

