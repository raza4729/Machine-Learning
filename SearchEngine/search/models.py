from django.db import models

# Create your models here.
class Search(models.Model):
    topic = models.CharField(max_length=100)
