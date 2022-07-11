from dataclasses import field
from django import forms
from item.models import item
class ItemForm(forms.ModelForm):
    class Meta:
        model=item
        fields="__all__"