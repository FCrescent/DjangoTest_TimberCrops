from django.shortcuts import render, redirect, get_object_or_404
from .forms import GameModeForm, ModifyGameModeForm#, ModifyLockForm
from .models import GameMode
import logging
from django.contrib import messages
from django.http import HttpRequest
# Create your views here.


from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, TimberCrops!")

def home(request):
    return render(request, 'home.html')

def settings_hub(request: HttpRequest) -> HttpResponse: #type hinting used to specify the expected type of the request
    form = GameModeForm()
    
    if request.method == 'POST':
        form = GameModeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_hub')

    existing_game_modes = GameMode.objects.all()

    context = {'form': form, 'existing_game_modes': existing_game_modes}
    return render(request, 'settings_hub.html', context)

def modify_game_mode(request, game_mode_id):
    game_mode = get_object_or_404(GameMode, id=game_mode_id)
    
    if request.method == 'POST':
        form = ModifyGameModeForm(request.POST, instance=game_mode)
        if form.is_valid():
            form.save()
            return redirect('settings_hub')
    else:
        form = ModifyGameModeForm(instance=game_mode)

    return render(request, 'modify_game_mode.html', {'form': form, 'game_mode': game_mode})






def delete_game_mode(request):
    if request.method == 'POST':
        game_mode_id = request.POST.get('game_mode_id')
        # request
        if game_mode_id:
            GameMode.objects.filter(id=game_mode_id).delete()
    return redirect('settings_hub')  # Redirect back to the settings hub