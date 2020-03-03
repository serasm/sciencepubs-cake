from django.http import HttpResponse
from django.shortcuts import render
from excel30882.models import Publication
from excel30882.models import PublicationCategory

import requests

# Publikacje - ich spis
def index(request):
    categorydisplay30991 = Publication.objects.all()

    data = {
        'PublicationName': 'Publikacje',
        'Publication': categorydisplay30991
    }

    return render(request,'categorydisplay30991/index.html', data)

# Kategorie - ktore powinny sie wyswietlac
def category(request, PublicationId):
    mypub = Publication.objects.get(pk=PublicationId)
    publist = mypub.PublicationCategories.all()

    context = {
        'CurrentPublication': mypub.publicationName,
        'Categories': list(publist)
    }

    return render(request, 'categorydisplay30991/category.html', context)