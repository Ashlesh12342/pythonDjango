""" drf example """
from rest_framework import serializers
from poc.models import Person, Species

class PersonSerializer(serializers.ModelSerializer):
    """ person serialiser """
    class Meta:
        """ person serialiser """
        model = Person
        fields = ('name', 'birth_year', 'eye_color', 'species')

class SpeciesSerializer(serializers.ModelSerializer):
    """ person serialiser """
    class Meta:
        """ person serialiser """
        model = Species
        fields = ('name', 'classification', 'language')
