from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password):
        user = self.model(username=username, github_username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=255, unique=True)
    github_username = models.CharField(max_length=255, unique=True)
    oauth_token = models.CharField(max_length=500)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    def get_short_name(self):
        return self.username

    def get_long_name(self):
        return self.username
