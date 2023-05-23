import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru'
    def get_api_key(self, email, password):
        headers = {
            'accept': 'application/json',
            'email' : email,
            'password' : password,


        }
        res = requests.get(self.base_url +'/api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def get_list_of_pet(self, auth_key, filter):
        headers = {'auth_key':auth_key['key']}
        filter = {'filter':filter}
        res = requests.get(self.base_url + '/api/pets', headers=headers, params  = filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

        res = requests.post(self.base_url + '/api/pets', headers=headers, data=data, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def delete_pet(self, auth_key:json, pet_id:str) -> json:
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url + f'/api/pets/{pet_id}', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def put_new_info_about_pet(self, auth_key: json,pet_id:str, name: str, animal_type: str, age: str) -> json:
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key['key']}
        res = requests.put(self.base_url + f'/api/pets/{pet_id}', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def new_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key['key']}
        res = requests.post(self.base_url + '/api/create_pet_simple', headers=headers, data = data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def add_photo_of_pet(self,auth_key: json,pet_id:str,pet_photo: str )-> json:

        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
        res = requests.post(self.base_url + f'/api/pets/set_photo/{pet_id}', headers=headers, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result