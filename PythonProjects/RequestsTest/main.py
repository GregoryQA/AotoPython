import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'YOUR_TOKEN'
TRAINER_ID = 'YOUR_ID'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "name",
    "photo_id": 1
}

response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.json())

body_rename = {
    "pokemon_id": "pokemon_id",
    "name": "newname",
    "photo_id": 1
}

response_rename = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_rename)
print(response_rename.json())

body_addp = {
    "pokemon_id": "pokemon_id"
}

response_addp = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_addp)
print(response_addp.json())