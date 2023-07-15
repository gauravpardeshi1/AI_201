import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import create_app

@pytest.fixture
def app() -> Flask:
    app = create_app()
    return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()

def test_get_weather_valid_city(client: FlaskClient):
    response = client.get('/weather/San Francisco')
    assert response.status_code == 200
    assert response.json == {'temperature': 14, 'weather': 'Cloudy'}

def test_get_weather_invalid_city(client: FlaskClient):
    response = client.get('/weather/InvalidCity')
    assert response.status_code == 404
    assert response.json == {'error': 'City not found'}