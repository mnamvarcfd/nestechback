from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.conf import settings


class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email.") 
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    
    
    
class TeamMembers(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name


class Services(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=400, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title


class BackgroundVideo(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    video = models.FileField(null=False, blank=False)
    
    def __str__(self) -> str:
        return self.title
