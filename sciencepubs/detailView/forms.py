from django import forms
from excel30882.models import Publication, PublicationCategory

class CzasopismaForm(forms.ModelForm):

    class Meta:
        model = Publication
        fields = '__all__'