from django import forms
from .models import GameMode, Need, NeedCat, ResourceCat, Resource

class GameModeForm(forms.ModelForm):
    class Meta:
        model = GameMode
        exclude = [] #includes all fields by default

class ModifyGameModeForm(forms.ModelForm):
    class Meta:
        model = GameMode
        exclude = []

class NeedCatForm(forms.ModelForm):
    class Meta:
        model = NeedCat
        fields = ['name']

class NeedForm(forms.ModelForm):
    class Meta:
        model = Need
        exclude = []

class ResourceCatForm(forms.ModelForm):
    class Meta:
        model = ResourceCat
        fields = ['name']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'resource_cat']