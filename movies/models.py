from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Genre name",
                            help_text='Enter a film genre (e.g. sci-fi, comedy)')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        """ Řetězec, který se používá jako textová reprezentace objektu (například v
       administraci aplikace).
        V našem případě bude objekt (žánr) reprezentován výpisem obsahu pole name """
        return self.name