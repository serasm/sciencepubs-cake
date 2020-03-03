from django.http import HttpResponse
from django.shortcuts import render
from excel30882.models import Publication
from excel30882.models import PublicationCategory
import requests
# Create your views here.



def index(request):
    pubcategoryview30890 = PublicationCategory.objects.all()

    data = {
    'PublicationCategoryName': 'Kategorie',
    'PublicationCategory': pubcategoryview30890
    }

    return render(request,'pubcategoryview30890/index.html', data)


def publication(request, PublicationCategoryId):
    try:
        Category = PublicationCategory.objects.get(pk=PublicationCategoryId)
    except PublicationCategory.DoesNotExist:
        raise Http404("PublicationCategory does not exist")
    
    context = {
        'Kategoria' : Category.PublicationCategoryName,
        'Publication': list(Category.publication_set.all())
    }

    return render(request, 'pubcategoryview30890/publication.html', context)


