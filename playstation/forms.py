from dataclasses import field
from django import forms
from playstation.models import playstation
class ItemForm(forms.ModelForm):
    class Meta:
        model=playstation
        fields="__all__"