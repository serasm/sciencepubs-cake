from excel30882.models import Publication
from .forms import SearchForm
from django.shortcuts import render
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from django.template import loader
from django.http import HttpResponse

class Searchfilters(BaseFilter):
    search_fields = {
        'searchfield' : ['publicationName', 'publicationIssn', 'publicationEissn', 'publicationName2']
    }

class SearchList(SearchListView):
    model = Publication
    paginate_by = 30
    template_name = "search.html"
	
    form_class = SearchForm
    filter_class = Searchfilters
	
