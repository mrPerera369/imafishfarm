# bought/forms.py
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Item
        fields = ['date', 'name','quantity']
