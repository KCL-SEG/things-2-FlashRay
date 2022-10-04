from django import forms
from .models import Thing
from django.utils.translation import gettext_lazy as _

class FormUpForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description' : forms.Textarea(),
        }
        labels = {
            'quantity' : _('Number Input')
        }