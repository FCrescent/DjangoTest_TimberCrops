from django import forms
from .models import ( 
    GameMode, Need, Resource, NatStruct,
    NeedCat, ResourceCat, NatStructCat    
)

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

class NatStructCatForm(forms.ModelForm):
    class Meta:
        model = NatStructCat
        fields = ['name']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'category']

class NatStructForm(forms.ModelForm):
    resource_cut = forms.ModelChoiceField(queryset=Resource.objects.all(), required=False)
    resource_cut_yield = forms.IntegerField(required=False)
    resource_harvest = forms.ModelChoiceField(queryset=Resource.objects.all(), required=False)
    days_between_harvest = forms.IntegerField(required=False)        
    resource_harvest_yield = forms.IntegerField(required=False)
    
    class Meta:
        model = NatStruct
        fields = ['name', 'category', 'days_to_grow', 'resource_cut', 'resource_cut_yield',
                  'resource_harvest', 'days_between_harvest', 'resource_harvest_yield']
        
       
