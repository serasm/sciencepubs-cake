from django.db import models

# Create your models here.
class PublicationCategory(models.Model):
    PublicationCategoryId = models.IntegerField()
    PublicationCategoryName = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.PublicationCategoryName}"


class Publication(models.Model):
    publicationName = models.CharField(max_length=256)
    publicationIssn = models.CharField(max_length=9)
    publicationEissn = models.CharField(max_length=9)
    publicationName2 = models.CharField(max_length=256)  
    publicationIssn2 = models.CharField(max_length=9)
    publicationEissn2 = models.CharField(max_length=9)  
    PublicationPoints = models.IntegerField()
    PublicationCategories = models.ManyToManyField(PublicationCategory, blank=True)

    def __str__(self):
        return f"{self.publicationName}"