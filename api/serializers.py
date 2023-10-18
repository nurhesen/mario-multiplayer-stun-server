from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'username', 'x', 'y']

    def update(self, instance, validated_data):
        # # Update the existing instance with the validated data
        instance.username = validated_data.get('username', instance.username)
        instance.x = validated_data.get('x', instance.x)
        instance.y = validated_data.get('y', instance.y)

        # Save and return the updated instance
        instance.save()                                                                                                                                                                                                                                                                                                               
        return instance