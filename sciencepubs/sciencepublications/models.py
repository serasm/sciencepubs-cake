from django.db import models

from rest_framework import serializers
import uuid

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.PublicationCategoryName}"

    def validate_name(self, value):
        qs = Category.object.filter(name__iexact=value)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("The title must be unique")


class Publication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    issn = models.CharField(max_length=9)
    eissn = models.CharField(max_length=9)
    name2 = models.CharField(max_length=256)
    issn2 = models.CharField(max_length=9)
    eissn2 = models.CharField(max_length=9)
    points = models.IntegerField()
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f"{self.publicationName}"

