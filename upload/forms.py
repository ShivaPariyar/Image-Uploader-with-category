from django import forms
from .models import *


class ImageForms(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {
            'photo' : ''
        }
