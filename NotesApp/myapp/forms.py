from dataclasses import fields
from pyexpat import model
from .models import mynotes
from django import forms

class noteform(forms.ModelForm):
    class Meta:
        model=mynotes
        fields=['topic','title','note']

        widgets={
            'topic':forms.TextInput(attrs={'class':'form-control border-dark border-1 alert-info'}),
            'title':forms.TextInput(attrs={'class':'form-control border-dark border-1 alert-info'}),
            'note':forms.Textarea(attrs={'class':'form-control border-dark border-1 alert-info'})
        }