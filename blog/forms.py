from django import forms
from django.forms import ModelForm
from .models import *


class ListForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    class Meta:
        model = List
        fields = '__all__'