from django import forms
from .models import CareLog
from .models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        exclude = ['user']


class CareLogForm(forms.ModelForm):
    class Meta:
        model = CareLog
        fields = ["date", "notes"]
