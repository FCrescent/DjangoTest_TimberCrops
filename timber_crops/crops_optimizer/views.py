from django.shortcuts import render, redirect
from .forms import GameModeForm
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

def delete_game_mode(request):
    if request.method == 'POST':
        game_mode_id = request.POST.get('game_mode_id')
        # request
        if game_mode_id:
            GameMode.objects.filter(id=game_mode_id).delete()
    return redirect('settings_hub')  # Redirect back to the settings hub