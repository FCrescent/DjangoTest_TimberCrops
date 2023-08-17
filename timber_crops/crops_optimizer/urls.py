from django.urls import path
from .views import views, views_resource_cat

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('settings-hub/', views.settings_hub, name='settings_hub'),
    path('delete-game-mode/', views.delete_game_mode, name='delete_game_mode'),
    path('modify-game-mode/<int:game_mode_id>/', views.modify_game_mode, name='modify_game_mode'),
    path('resource-category/', views_resource_cat.ResourceCatListView.as_view(), name='resource_cat_list'),
    path('resource-category/create/', views_resource_cat.ResourceCatCreateView.as_view(), name='resource_cat_create'),
    path('resource-category/<int:pk>/update/', views_resource_cat.ResourceCatUpdateView.as_view(), name='resource_cat_update'),
    path('resource-category/<int:pk>/delete/', views_resource_cat.ResourceCatDeleteView.as_view(), name='resource_cat_delete'),
]
