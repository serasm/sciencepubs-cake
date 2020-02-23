from django.db import models

# Create your models here.
class Simple(models.Model):
    text = models.CharField(max_length=50)

class Publication(models.Model):
    publicationName = models.CharField(max_length=256)
    publicationIssn = models.CharField(max_length=8)
    publicationEissn = models.CharField(max_length=8)