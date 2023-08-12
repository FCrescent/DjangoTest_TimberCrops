from django.shortcuts import render, redirect, get_object_or_404
from .forms import GameModeForm, ModifyGameModeForm
from .models import GameMode
# Create your views here.


from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, TimberCrops!")

def home(request):
    return render(request, 'home.html')

# def settings_hub(request):
#     return render(request, 'settings_hub.html')
def settings_hub(request):
    form = GameModeForm()

    if request.method == 'POST':
        form = GameModeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_hub')

    existing_game_modes = GameMode.objects.all()

    # context = {'form': form}
    context = {'form': form, 'existing_game_modes': existing_game_modes}
    return render(request, 'settings_hub.html', context)

def modify_game_mode(request, game_mode_id):
    game_mode = get_object_or_404(GameMode, id=game_mode_id)
    if request.method == 'POST':
        form = ModifyGameModeForm(request.POST, instance=game_mode)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            if new_name != game_mode.name and GameMode.objects.filter(name=new_name).exists():
                form.add_error('name', 'A Game Mode with this name already exists.')
            else:
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