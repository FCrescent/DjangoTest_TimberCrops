from django import forms
from .models import GameMode, Need, NeedsCategory, ResourceCat

class GameModeForm(forms.ModelForm):
    class Meta:
        model = GameMode
        exclude = [] #includes all fields by default

class ModifyGameModeForm(forms.ModelForm):
    class Meta:
        model = GameMode
        exclude = []

class NeedsCategoryForm(forms.ModelForm):
    class Meta:
        model = NeedsCategory
        exclude = []

class NeedForm(forms.ModelForm):
    class Meta:
        model = Need
        exclude = []

class ResourceCatForm(forms.ModelForm):
    class Meta:
        model = ResourceCat
        fields = ['name']