import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'YOUR_TOKEN'
TRAINER_ID = 'YOUR_ID'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

def test_status_traners():
    response=requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_name_in_traners():
    response_get=requests.get(url=f'{URL}/trainers', params = {'trainer_id' : 'YOUR_ID'})
    assert response_get.json()["data"][0]["id"] == 'YOUR_ID'
    