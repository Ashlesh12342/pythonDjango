""" testing """
from rest_framework import viewsets

from poc.serializers import PersonSerializer, SpeciesSerializer
from poc.models import Person, Species

class PersonViewSet(viewsets.ModelViewSet):
    """ testing """
    queryset = Person.objects.all() # pylint: disable=no-member
    serializer_class = PersonSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    """ testing """
    queryset = Species.objects.all() # pylint: disable=no-member
    serializer_class = SpeciesSerializer
