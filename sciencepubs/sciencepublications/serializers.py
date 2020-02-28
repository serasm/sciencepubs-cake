from rest_framework import serializers
from .models import Publication, Category

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id', 'name', 'issn',
                  'eissn', 'name2', 'issn2',
                  'eissn2', 'points', 'categories')

        read_only_fields = ['id']

        def validate_issn(self, value):
            qs = Publication.objects.filter(issn__iexact=value)
            if self.instance:
                qs = qs.exclude(id=self.instance.id)
            if qs.exists():
                raise serializers.ValidationError("The ISSN must be unique")

            return  value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'catind')

        read_only_fields = ['id']

        def validate_name(self, value):
            qs = Category.objects.filter(name__iexact=value)

            if qs.exists():
                raise serializers.ValidationError("The name must be unique")

            return  value