import requests

token = '8fc0fcbbcc02ca80d437ba30f1e4a542'
base_url = 'https://pokemonbattle.me:9104/'
pokemon_id = '9520'

# регистрация тренера
'''response = requests.post(f'{base_url}trainers/reg', json={
    'trainer_token': token,
    'email': 'vika@mail.ru',
    'password': 'Iloveqa1'
})

print(response.status_code)'''

# активация тренера (подтверждение почты)
'''response_activated = requests.post(f'{base_url}trainers/confirm_email', json={
    'trainer_token': token
})

print(response_activated.text)
'''

# создание покемона
response_add_pokemon = requests.post(f'{base_url}pokemons', headers={'trainer_token': token}, json={
    'name': 'ПикаПика',
    'photo': 'https://dolnikov.ru/pokemons/albums/001.png'
})
print(response_add_pokemon.text)


# получение информации по покемонам
'''response_pokemon = requests.get(f'{base_url}pokemons', params={'trainer_id': 4125})
print(response_pokemon.text)
'''

# смена имени покемона
response_update_name_pokemon = requests.put(f'{base_url}pokemons', headers={'trainer_token': token}, json={
    'pokemon_id': pokemon_id,
    'name': 'Bulbik',
    'photo': 'https://dolnikov.ru/pokemons/albums/008.png'
})
print(response_update_name_pokemon.text)

# ловля покемона в покебол
response_catch_pokemon = requests.post(f'{base_url}trainers/add_pokeball', headers={'trainer_token': token}, json={
    'pokemon_id': pokemon_id
})
print(response_catch_pokemon.text)

