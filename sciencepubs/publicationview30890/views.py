from django.http import HttpResponse
from django.shortcuts import render
from excel30882.models import Publication
from excel30882.models import PublicationCategory
import requests
# Create your views here.

def index(request):
    #publicationview30890 = Publication.objects.all()
    api_url = "http://127.0.0.1:8000/api/sciencepublications/publications/"
    publicationview30890 = requests.get(api_url)

    data = {
    'publicationName': 'Publikacje',
    'Publication': publicationview30890
    }

    return render(request,'publicationview30890/index.html', data)