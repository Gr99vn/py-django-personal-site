from django.db import models
from django.db.models.base import Model

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  technology = models.CharField(max_length=25)
  image = models.FilePathField(path="/img")

  def __str__(self):
      return self.title