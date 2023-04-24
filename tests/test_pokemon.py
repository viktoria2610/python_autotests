import requests
import pytest

BASE_URL = 'https://pokemonbattle.me:9104/'
TRAINER_ID = 4125

# проверка, что ответ гет запроса приходит с кодом 200
def test_status_code():
    response = requests.get(f'{BASE_URL}trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

# проверка правильности имени тренера и города
@pytest.mark.parametrize('key, value', [('trainer_name', 'Vikki'), ('city', 'Saint-P')])

def test_parts_of_body(key, value):
    response = requests.get(f'{BASE_URL}trainers', params={'trainer_id': TRAINER_ID})
    assert response.json()[key] == value
