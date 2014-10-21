from django import forms
from collect.models import Collection

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        exclude = ['user']

