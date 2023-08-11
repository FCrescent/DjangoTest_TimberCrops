from django import forms
from .models import GameMode

class GameModeForm(forms.ModelForm):
    class Meta:
        model = GameMode
        fields = ['name', 'food_consumption_percentage', 'food_consumption_daily_unit']
