from dataclasses import field
from django import forms
from xbox.models import xbox
class ItemForm(forms.ModelForm):
    class Meta:
        model=xbox
        fields="__all__"