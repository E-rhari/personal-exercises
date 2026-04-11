from django.db import models

class Sushi(models.Model):
    sushi    = models.CharField(max_length=20)
    chirashi = models.IntegerField()

    def __str__(self) -> str:
        return self.sushi