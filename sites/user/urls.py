from django.conf.urls import patterns, include, url

from sites.user import views


urlpatterns = patterns('',
    url(r'^$', views.LoginView.as_view(), name="user-login"),
)

