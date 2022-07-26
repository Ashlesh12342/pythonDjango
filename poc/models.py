""" unit testing"""
from django.db import models

# Create your models here.
class Species(models.Model):
    """" Species """
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        """ string representation"""
        return f'{self.name}'

class Person(models.Model):
    """ person  """
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=10)
    eye_color = models.CharField(max_length=10)
    species = models.ForeignKey(Species, on_delete=models.DO_NOTHING)
