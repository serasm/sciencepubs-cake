from excel30882.models import Publication
from django import forms

class SearchForm(forms.Form):
    searchfield =  forms.CharField(
                    required = False,
                    label='Search publications (by name, ISSN or EISSN)',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )
