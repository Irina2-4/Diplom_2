import pytest
import requests
import allure
from urls import Urls, Endpoints
from conftest import user
from data import GenerateUser

class TestChangeDataUser:
    @allure.title('Изменение данных авторизованного пользователя. Позитивный тест')
    @pytest.mark.parametrize('data',[GenerateUser.generate_user_data()["name"],
                             GenerateUser.generate_user_data()["password"],
                             GenerateUser.generate_user_data()["email"]])

    def test_change_data_user_with_authorization(self,user,data):
        token = user[1].json()["accessToken"]
        assert token
        headers = {'Authorization': token}
        response = requests.patch(f'{Urls.MAIN_URL}{Endpoints.CHANGE_USER_DATA}',headers=headers,data=data)
        assert response.status_code == 200

    @allure.title('Изменение данных пользователя без авторизации. Негативный тест')
    @pytest.mark.parametrize('data',[GenerateUser.generate_user_data()["name"],
                             GenerateUser.generate_user_data()["password"],
                             GenerateUser.generate_user_data()["email"]])

    def test_change_data_user_without_authorization(self,data):
        response = requests.patch(f'{Urls.MAIN_URL}{Endpoints.CHANGE_USER_DATA}', data=data)
        assert response.status_code == 401 and response.json()["success"] is False
