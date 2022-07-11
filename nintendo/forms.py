from dataclasses import field
from django import forms
from nintendo.models import nintendo
class ItemForm(forms.ModelForm):
    class Meta:
        model=nintendo
        fields="__all__"