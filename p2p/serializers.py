# serializers.py
from rest_framework import serializers
from .models import Offer, Answer

class Offererializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = [ 'offer', 'index','host_uuid']
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer', 'index','host_uuid']