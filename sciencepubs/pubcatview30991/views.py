from django.http import HttpResponse
from django.shortcuts import render
from excel30882.models import PublicationCategory
import requests

# Create your views here.
def index(request):
    #pubcatview30991 = PublicationCategory.objects.all()
   # api_url = "http://127.0.0.1:8000/api/sciencepublications/categories/"
    pubcatview30991 = PublicationCategory.objects.all()       #requests.get(api_url)

    data = {
    'publicationCategoryName': 'Kategorie',
    'PublicationCategory': pubcatview30991
    }

    return render(request,'pubcatview30991/index.html', data)