import base64
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import os


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email, password):
        headers = {
            'email': email,
            'password': password
        }
        endpoint = 'api/key'
        res = requests.get(self.base_url + endpoint, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_api_pets(self, auth_key, filter):
        headers = {
            "auth_key": auth_key['key']
        }
        filter = {
            "filter": filter
        }
        endpoint = 'api/pets'
        res = requests.get(self.base_url+endpoint, headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_api_pets(self, auth_key, name, animal_type, age, pet_photo):

        data = MultipartEncoder(
            formdata={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': pet_photo
            })
        headers = {
            'auth_key': auth_key['key'],
            'Content-Type': data.content_type
        }
        endpoint = 'api/pets'
        res = requests.post(self.base_url + endpoint, headers=headers, data=formdata)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
            print(result)
        return status, result

    def post_api_pets_set_photo_pet_id(self, auth_key, pet_id, pet_photo):
        headers = {
            'auth_key': auth_key
        }

        formdata = {
            'pet_photo': pet_photo
        }
        endpoint = 'api/pets/set_photo/pet_id'
        res = requests.post(self.base_url + endpoint, headers=headers, data=formdata)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
        статус запроса и результат в формате JSON с текстом уведомления о успешном удалении.
        На сегодняшний день тут есть баг - в result приходит пустая строка, но status при этом = 200"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: int) -> json:
        """Метод отправляет запрос на сервер о обновлении данных питомуа по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except
            result = res.text
        return status, result
