import allure
from urls import Urls, Endpoints
from conftest import user
import requests
from helpers import GenerateUser

class TestLoginUser:

    @allure.title('Авторизация пользователя. Позитивный тест')
    def test_authorization_user(self,user):
        payload = GenerateUser.generate_user_data()
        requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_USER}', data=payload)
        response = requests.post(f'{Urls.MAIN_URL}{Endpoints.LOGIN_USER}', data=payload)
        assert response.status_code == 200
        assert response.json()["success"] is True


    @allure.title('Авторизация пользователя с несуществующей парой логин-пароль. Негативный тест')
    def test_authorization_error_if_no_name(self,user):
          user = GenerateUser.generate_user_data()
          response =  requests.post(f'{Urls.MAIN_URL}{Endpoints.LOGIN_USER}',data=user)
          assert response.status_code == 401
          assert response.json()["message"] == "email or password are incorrect"