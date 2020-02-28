from .serializers import PublicationSerializer, CategorySerializer
from .models import Publication, Category
from rest_framework import  generics, mixins
from django.db.models import Q

class PublicationPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PublicationSerializer

    def get_queryset(self):
        qs = Publication.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(name__icontains=query) | Q(issn__icontains=query)
                           | Q(eissn__icontains=query) | Q(name2__icontains=query)).distinct()

        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PublicationRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PublicationSerializer

    def get_queryset(self):
        return Publication.objects.all()

class CategoriesPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = CategorySerializer

    def get_queryset(self):
        qs = Category.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(name__icontains=query))

        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CategoriesRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = CategorySerializer

    def get_queryset(self):
        return  Category.objects.all()