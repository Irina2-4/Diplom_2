import random
import string
class GenerateUser:


    @staticmethod
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod

    def generate_user_data():
    # генерируем логин, пароль и имя пользователя
        email = f'{GenerateUser.generate_random_string(10)}{'@yandex.ru'}'
        password = GenerateUser.generate_random_string(10)
        name = GenerateUser.generate_random_string(10)

    # собираем тело запроса
        payload = {
            "email": email,
            "password": password,
            "name": name
             }
        return payload

    @staticmethod
    def generate_user_without_email():
    # генерируем логин, пароль и имя курьера
        password = GenerateUser.generate_random_string(10)
        name = GenerateUser.generate_random_string(10)
    # собираем тело запроса
        payload = {
            "password": password,
            "name": name
             }
        return payload

    @staticmethod
    def generate_user():
        # генерируем логин, пароль и имя пользователя
        email = f'{GenerateUser.generate_random_string(10)}{'@yandex.ru'}'
        password = GenerateUser.generate_random_string(10)
        name = GenerateUser.generate_random_string(10)

        # собираем тело запроса
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

    @staticmethod
    def generate_email():
        email = f'{GenerateUser.generate_random_string(10)}{'@yandex.ru'}'
        payload = { "email": email}
        return payload

class Ingredients:
    ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa72","61c0c5a71d1f82001bdaaa79"]
    }
    wrong_hash = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6r", "61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa99"]
                          }
    without_ingredients = {"ingredients":[]}