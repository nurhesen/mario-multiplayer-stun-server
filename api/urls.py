from django.urls import path
from .views import PlayerCreateAPIView, PlayerUpdateAPIView, PlayerListAPIView

urlpatterns = [
    path('players/', PlayerCreateAPIView.as_view(), name='player-create'),
    path('players/all/', PlayerListAPIView.as_view(), name='player-list'),

    path('players/<str:username>/', PlayerUpdateAPIView.as_view(), name='player-update'),

]
