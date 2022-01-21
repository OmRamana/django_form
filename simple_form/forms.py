from re import L
from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

