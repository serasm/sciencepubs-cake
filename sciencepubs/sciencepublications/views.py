from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests
import json

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
    return HttpResponse(response)
    #return response