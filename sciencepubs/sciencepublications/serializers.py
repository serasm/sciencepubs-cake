from rest_framework import serializers
from excel30882.models import Publication, PublicationCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationCategory
        fields = '__all__'

        read_only_fields = ['PublicationCategoryId']

        def validate_name(self, value):
            qs = PublicationCategory.objects.filter(PublicationCategoryName__iexact=value)

            if qs.exists():
                raise serializers.ValidationError("The name must be unique")

            return  value

class PublicationSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = '__all__'

        def validate_issn(self, value):
            qs = Publication.objects.filter(publicationIssn__iexact=value)
            if qs.exists():
                raise serializers.ValidationError("The ISSN must be unique")

            return  value