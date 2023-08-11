from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('settings-hub/', views.settings_hub, name='settings_hub'),
    path('delete-game-mode/', views.delete_game_mode, name='delete_game_mode'),

]
