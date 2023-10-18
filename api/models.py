from django.db import models

# Create your models here.
class Player(models.Model):
    username=models.CharField(max_length=260, unique=True)
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self) -> str:
        return self.username