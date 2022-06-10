from django.db import models

# Modelar de acuerdo a la lista de pokemones


class PokemonModel(models.Model):
    pokemon_id = models.IntegerField()
    pokemon_name = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    base_stats = models.JSONField(blank=True)
    evolutions = models.JSONField(blank=True)

