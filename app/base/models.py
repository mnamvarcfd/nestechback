from django.db import models
from django.contrib.auth.models import User


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
