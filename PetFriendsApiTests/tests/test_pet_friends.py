from settings import valid_email, valid_password
import requests
from api import PetFriends
import json
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder

pf = PetFriends()



def test_get_api_key(email=valid_email, password=valid_password):
    """Задаем логин и пароль для входа"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert "key" in result

def test_get_api_pets(filter = ""):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_api_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_post_add_new_pets(name='Лия', animal_type='кошка', age='4', pet_photo='images\cat1.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name']


