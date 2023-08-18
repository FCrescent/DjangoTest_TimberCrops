from django.shortcuts import render, redirect, get_object_or_404
from ..forms import GameModeForm, ModifyGameModeForm#, ModifyLockForm
from ..models import GameMode
import logging
from django.contrib import messages
from django.http import HttpRequest
from decimal import Decimal
# Create your views here.


from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, TimberCrops!")

def home(request):
    game_modes = GameMode.objects.all()
    context = {
        'game_modes': game_modes,
    }
    if request.method == 'POST':
        number_of_beavers = int(request.POST.get('number_of_beavers'))
        carrots_selected = 'carrots' in request.POST
        carrots_food_ratio = int(request.POST.get('carrots_food_ratio'))
        bread_selected = 'bread' in request.POST
        bread_food_ratio = int(request.POST.get('bread_food_ratio'))

        selected_game_mode_id = int(request.POST.get('game_mode'))
        try:
            selected_game_mode = GameMode.objects.get(pk=selected_game_mode_id)
        except GameMode.DoesNotExist:
            # Gérer le cas où le mode de jeu n'existe pas
            pass
        else:
            daily_food_intake = selected_game_mode.food_consumption_daily_unit
        # daily_food_intake = 2.5
        number_daily_food = daily_food_intake * number_of_beavers

        foods = {
            "carrots" : {
                "selected" : carrots_selected,
                "ratio_to_food" : carrots_food_ratio,
                "crop_yield" : 3,
                "days_between_harvest" : 4,
                "transformation_multiplier" : 1
            },
            "bread" : {
                "selected" : bread_selected,
                "ratio_to_food" : bread_food_ratio,
                "crop_yield" : 3,
                "days_between_harvest" : 10,
                "transformation_multiplier" : 5
            }
        }

        sum_food_ratio = sum(food_data["ratio_to_food"] for food_data in foods.values())

        for food_name, food_data in foods.items():
            if food_data["selected"]:
                ratio_to_food = food_data["ratio_to_food"]
                crop_yield = food_data["crop_yield"]
                days_between_harvest = food_data["days_between_harvest"]
                transformation_multiplier = food_data["transformation_multiplier"]

                required_daily_food_prod = ratio_to_food * number_daily_food / sum(food["ratio_to_food"] for food in foods.values())
                daily_crop_prod = crop_yield / days_between_harvest * transformation_multiplier
                required_crops_number = Decimal(required_daily_food_prod) / Decimal(daily_crop_prod)

                food_data["required_crops_number"] = required_crops_number
            else:
                food_data["required_crops_number"] = 0

        result_context = {
            'number_of_beavers': number_of_beavers,
            'carrots_selected': carrots_selected,
            'bread_selected': bread_selected,
            'required_carrot_crops': foods["carrots"]["required_crops_number"],
            'required_wheat_crops': foods["bread"]["required_crops_number"],
            # Add other variables here
            }    

        context = {**context, **result_context}

        return render(request, 'home.html', context)

    return render(request, 'home.html', {'game_modes': game_modes})


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