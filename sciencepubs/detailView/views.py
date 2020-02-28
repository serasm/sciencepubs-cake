from django.shortcuts import render
from .forms import CzasopismaForm
from excel30882.models import Publication, PublicationCategory
import requests
# Create your views here.
def details(request):
	api_url = "http://127.0.0.1:8000/api/sciencepublications/publications/"
	pubs = requests.get(api_url)

    #context = {'publications':Publication.objects.all()}
	context = {'publications': pubs}
	return render(request,"detailView/index.html",context)