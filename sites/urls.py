from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'docserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^project/', include('sites.project.urls')),
    url(r'^github/', include('sites.github.urls')),
    url(r'^user/', include('sites.user.urls')),
)
