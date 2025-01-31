import allure
from conftest import user,user_without_email
from urls import Urls,Endpoints
import requests
from helpers import GenerateUser

class TestCreateUser:

    @allure.title('Создание пользователя. Позитивный тест')
    def test_create_user(self,user):
        payload = GenerateUser.generate_user_data()
        response = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_USER}',data=payload)
        token = response.json()["accessToken"]
        assert response.status_code == 200
        assert response.json()["success"] is True
        requests.delete(f'{Urls.MAIN_URL}{Endpoints.DELETE_USER}', headers={'Authorization': f'{token}'})


    @allure.title('Создание пользователя без заполнения поля email. Негативный тест')
    def test_create_user_without_email(self, user_without_email):
        payload = GenerateUser.generate_user_without_email()
        response = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_USER}', data=payload)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"


    @allure.title('Создание ранее зарегистрированного пользователя. Негативный тест')
    def test_create_double_user(self,user):
        payload = GenerateUser.generate_user_data()
        response_poz = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_USER}',data = payload)
        token = response_poz.json()["accessToken"]
        response_neg = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_USER}', data=payload)
        assert response_neg.status_code == 403
        assert response_neg.json()["message"] == "User already exists"
        requests.delete(f'{Urls.MAIN_URL}{Endpoints.DELETE_USER}', headers={'Authorization': f'{token}'})