from django.conf.urls import patterns, include, url
from django.contrib import admin

from sites import views


urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^project/', include('sites.project.urls')),
    url(r'^github/', include('sites.github.urls')),
    url(r'^user/', include('sites.user.urls')),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
)
