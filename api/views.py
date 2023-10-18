from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView,ListAPIView
from .models import Player
from .serializers import PlayerSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PlayerCreateAPIView(ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_queryset(self):
        username = self.request.data.get('username')
        if username:
            return Player.objects.filter(username=username)
        return super().get_queryset()



class PlayerUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'username'



class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer