from django import forms
from .models import GameMode

class GameModeForm(forms.ModelForm):
    class Meta:
        model = GameMode
        exclude = [] #includes all fields by default

class ModifyGameModeForm(forms.ModelForm):
    class Meta:
        model = GameMode
        exclude = []

