import pytest
from data import GenerateUser
import requests
from urls import Urls, Endpoints

@pytest.fixture(scope ='function')
def user():
    payload = GenerateUser.generate_user_data() #Генерируем данные нового пользователя
    response = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_USER}',data=payload) #Отправка запроса для создания пользователя
    yield payload, response #Возвращаем данные в ответ на запрос
    token = response.json()["accessToken"] #Извлекаем токен из ответа для удаления пользователя
    requests.delete(f'{Urls.MAIN_URL}{Endpoints.DELETE_USER}', headers={'Authorization': f'{token}'}) #Отправляем Delete запрос для удаления пользователя

@pytest.fixture(scope ='function')
def user_without_email():
    payload = GenerateUser.generate_user_without_email()#Генерируем данные нового пользователя не указывая email
    response = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_USER}',data=payload)#Отправка запроса для создания пользователя
    yield payload, response #Возвращаем данные в ответ на запрос