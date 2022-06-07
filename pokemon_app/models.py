from django.db import models


class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=100)
    heigth = models.DecimalField(max_digits=5, decimal_places=2)
    weigth = models.DecimalField(max_digits=5, decimal_places=2)
    base_stats = models.TextField()
    preevolution_id = models.IntegerField()
    evolution_id = models.IntegerField()



