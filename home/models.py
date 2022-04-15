from django.db import models

# Create your models here.
class Polymodel(models.Model):
    polygon1 = models.JSONField(max_length=255)
    polygon2 = models.JSONField(max_length=255)