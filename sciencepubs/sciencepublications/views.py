from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests
import json
from .models import Publication

# Create your views here.
def index(request):
    template = loader.get_template('publications/index.html')
    return HttpResponse(template.render())

def sendRequest(request):
    URL = "api.elsevier.com/content/search/scopus"
    PARAMS = {
        'query': 'all(gene)',
        'apiKey': '15cc00bb996e844d8f6c871451bbd069'
    }
    response = requests.get('https://api.elsevier.com/content/search/scopus?query=all(gene)&apiKey=15cc00bb996e844d8f6c871451bbd069')
    #return HttpResponse(response)
    return response

def ImportPublications(request):
    apirequest = sendRequest(request)
    data = apirequest.json()
    Publicatons = data['search-results']['entry']
    x=len(Publicatons)-1
    y=x
    while x>0:
        a=Publication()
        a.publicationName=Publicatons[x]['dc:title']
        if 'prism:issn' in Publicatons[x]:
            a.publicationIssn=Publicatons[x]['prism:issn']
        if 'prismeIssn' in Publicatons[x]:
            a.publicationEissn=Publicatons[x]['prism:eIssn']
        a.save()
        x-=1
    return HttpResponse(f"Zaimportowano {y} publikacji do bazy")