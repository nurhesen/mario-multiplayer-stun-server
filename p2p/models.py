from django.db import models


class Offer(models.Model):
    offer = models.TextField()
    index = models.TextField()
    host_uuid = models.TextField()
    active_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.index)


class Answer(models.Model):
    answer = models.TextField()
    index = models.TextField()
    host_uuid = models.TextField()

    def __str__(self) -> str:
        return str(self.index)