from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_weather_valid_city(client):
    response = client.get('/weather/San Francisco')
    assert response.status_code == 200
    assert response.get_json() == {'temperature': 14, 'weather': 'Cloudy'}

def test_get_weather_invalid_city(client):
    response = client.get('/weather/Invalid City')
    assert response.status_code == 404
    assert response.get_json() == {'error': 'City not found'}