from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
pf = PetFriends()
# def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
#     status, result = pf.get_api_key(email, password)
#     assert status == 200
#     assert 'key' in result
# def test_get_all_pets_with_valid_key(filter = ""):
#     _, auth_key = pf.get_api_key(valid_email,valid_password)
#     status, result = pf.get_list_of_pet(auth_key, filter)
#     assert status == 200
#     assert len(result['pets']) > 0
# def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
#                                      age='4', pet_photo='images/cat1.jpg'):
#     """Проверяем что можно добавить питомца с корректными данными"""
#
#     # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     # Запрашиваем ключ api и сохраняем в переменую auth_key
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#
#     # Добавляем питомца
#     status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
#
#     # Сверяем полученный ответ с ожидаемым результатом
#     assert status == 200
#     assert result['name'] == name
# def test_succesful_delete_self_pet():
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pet(auth_key,"my_pets")
#     if len(my_pets['pets']) == 0:
#         pf.add_new_pet(auth_key, 'Baboyaga','evil', "3", "images/cat1.jpg")
#         _, my_pets = pf.get_list_of_pet(auth_key, "my_pets")
#     pet_id = my_pets['pets'][0]['id']
#     status,_ = pf.delete_pet(auth_key, pet_id)
#     _, my_pets = pf.get_list_of_pet(auth_key, "my_pets")
#     assert status == 200
#     assert pet_id not in my_pets.values()
# def test_valid_update_info_about_pet(name = 'пепега',animal_type='двортерьер',age='4',pet_photo='images/cat1.jpg'):
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pet(auth_key, "my_pets")
#     # pet_id = my_pets['pets'][0]['id']
#     if len(my_pets['pets']) > 0:
#         status, result = pf.put_new_info_about_pet(auth_key,my_pets['pets'][0]['id'],name,animal_type,age)
#         assert status == 200
#         assert result['name'] == name
#     else:
#         raise Exception('This is not my pet WTF')
# def test_valid_simple_new_pet_without_photo(name = 'Тестовая Пепега без фотки', animal_type = 'блохтерьер', age = '22'):
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     status, result = pf.new_pet_without_photo(auth_key, name, animal_type, age)
#     assert status == 200
#     assert result['name'] == name
# def test_valid_photo_update(pet_photo='images/P1040103.jpg'):
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pet(auth_key, "my_pets")
#     pet_id = my_pets['pets'][0]['id']
#     status, result = pf.add_photo_of_pet(auth_key,pet_id,pet_photo)
#     assert status == 200
# def test_get_API_key_with_invalid_login_and_password(email = invalid_email, password = invalid_password):
#     status, result = pf.get_api_key(email, password)
#     assert status == 403
# def test_invalid_data_without_photo(name = '', animal_type = '', age =''):
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     status, result = pf.new_pet_without_photo(auth_key, name, animal_type, age)
#     assert status == 400
# def test_get_all_pets_with_empty_API_key(filter = ""):
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     auth_key = {'key':''}
#     status, result = pf.get_list_of_pet(auth_key, filter)
#     print(auth_key)
#     assert status == 403
# def test_get_all_pets_with_invalid_API_key(filter = ""):
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     auth_key = {'key':'52ec8c4912900206b6b9cb7e0c819368e43b316e25995c22ffe1e44F'}
#     status, result = pf.get_list_of_pet(auth_key, filter)
#     print(auth_key)
#     assert status == 403
# def test_invalid_photo_update(pet_photo='images/cat_photo.txt'):
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pet(auth_key, "my_pets")
#     pet_id = my_pets['pets'][0]['id']
#     status, result = pf.add_photo_of_pet(auth_key,pet_id,pet_photo)
#     assert status == 500
# def test_succesful_delete_self_pet_with_empty_pet_id():
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pet(auth_key,"my_pets")
#     pet_id = ''
#     status,_ = pf.delete_pet(auth_key, pet_id)
#     assert status == 404
# def test_valid_update_info_with_someone_pet_id(name = 'пепега',animal_type='кто то',age='4'):
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pet(auth_key, "my_pets")
#     pet_id ='31961c16-ea58-434d-8f39-603b0b233761'
#     status, result = pf.put_new_info_about_pet(auth_key,pet_id,name,animal_type,age, )
#     assert status == 403
# def test_delete_someone_pet():
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pet(auth_key,"my_pets")
#     pet_id ='31961c16-ea58-434d-8f39-603b0b233761'
#     status,_ = pf.delete_pet(auth_key, pet_id)
#     _, my_pets = pf.get_list_of_pet(auth_key, "my_pets")
#     assert status == 403
#     assert pet_id  in my_pets.values()

# someone
# 31961c16-ea58-434d-8f39-603b0b233761