import requests
from data import Ingredients
import allure
from urls import Urls, Endpoints
from conftest import user

class TestCreateOrder:

    @allure.title('Создание заказа не авторизованным пользователем. Позитивный тест')
    def test_create_order_without_authorization(self):
        response = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_ORDER}', data=Ingredients.ingredients)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Создание заказа с неверным хешем ингредиентов. Негативный тест')
    def test_create_order_with_wrong_hash(self):
        response = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_ORDER}', data=Ingredients.wrong_hash)
        assert response.status_code == 500

    @allure.title('Создание заказа без добавления ингредиентов. Негативный тест')
    def test_create_order_without_ingredients(self):
        response = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_ORDER}', data=Ingredients.without_ingredients)
        assert response.status_code == 400 and response.json()["success"] is False

    @allure.title('Создание заказа без добавления ингредиентов. Негативный тест')
    def test_create_order_without_ingredients(self):
        response = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_ORDER}', data=Ingredients.without_ingredients)
        assert response.status_code == 400 and response.json()["success"] is False

    @allure.title('Создание заказа авторизованным пользователем. Позитивный тест')
    def test_create_order_with_authorization(self, user):
        token = user[1].json().get("accessToken")
        headers = {"Authorization": token}
        response = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_ORDER}', data=Ingredients.ingredients, headers= headers)
        assert response.status_code == 200 and response.json()["success"] is True
