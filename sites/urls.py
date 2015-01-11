from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from sites import views


urlpatterns = patterns('',
    url(r'^a/', views.IndexView.as_view(), name="homepage"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^project/', include('sites.project.urls')),
    url(r'^github/', include('sites.github.urls')),
    url(r'^user/', include('sites.user.urls')),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
)

from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
#    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#
#    urlpatterns += staticfiles_urlpatterns()
