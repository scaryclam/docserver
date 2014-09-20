from django.db import models


class GithubConf(models.Model):
    repo_uri = models.CharField(max_length=355)
    repo_name = models.CharField(max_length=255, blank=True, null=True)
    repo_key = models.CharField(max_length=255, blank=True, null=True)


class DocumentBuild(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Project(models.Model):
    name = models.CharField(max_length=255)
    github_conf = models.ForeignKey(GithubConf)
    document_build = models.ManyToManyField(DocumentBuild, 
                                            related_name="document_builds")

