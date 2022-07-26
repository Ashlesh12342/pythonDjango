""" test """
from django.urls import path, include
from rest_framework import routers
from poc.views import PersonViewSet, SpeciesViewSet
# from . import views

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('test', views.index, name='index'),
]
