from django import forms

from .models import ComentarioArticulo

from django.forms import ModelForm, ClearableFileInput, widgets

class ComentarioFormArticulo(forms.ModelForm):
    class Meta: 
        model = ComentarioArticulo
        fields = ['art','usuario','email','tel','dir']
