"""unit testing """
import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_post():
    """ test pytest"""
    payload = dict(
        name="type",
        classification="test",
        language="test"
    )

    response = client.post('/poc/species/', payload)

    data = response.data

    assert data['name'] == payload['name']
    assert data['classification'] == payload['classification']
    assert data['language'] == payload['language']

@pytest.mark.django_db
def test_get():
    """test get"""
    response = client.get('/poc/species/')
    assert response.status_code == 200
