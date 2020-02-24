from django.http import HttpResponse
from django.shortcuts import render
from excel30882.models import Publication
from excel30882.models import PublicationCategory
# Create your views here.

def index(request):
    publicationview30890 = Publication.objects.all()
    data = {
    'publicationName': 'Publikacje',
    'Publication': publicationview30890
    }

    return render(request,'publicationview30890/index.html', data)

  



