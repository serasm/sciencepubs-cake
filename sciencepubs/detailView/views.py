from django.shortcuts import render
from .forms import CzasopismaForm
from excel30882.models import Publication, PublicationCategory
import requests
# Create your views here.
def details(request):
	context = {'publications':Publication.objects.all()}
	return render(request,"detailView/index.html",context)