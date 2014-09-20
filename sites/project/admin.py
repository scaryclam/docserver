from django.contrib import admin

from sites.project import models


admin.site.register(models.Project)
admin.site.register(models.GithubConf)
