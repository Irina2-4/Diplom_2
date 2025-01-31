import allure
from urls import Urls,Endpoints
from conftest import user
import requests
from data import Ingredients

class TestGetOrderUser:
    @allure.title('Получение списка заказов неавторизованным пользователем. Негативный тест')
    def test_get_order_without_avtorization_user(self):
        response = requests.get(f'{Urls.MAIN_URL}{Endpoints.GET_ORDER}')
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"

    @allure.title('Получение списка заказов авторизованным пользователем. Позитивный тест')
    def test_get_order_with_authorization_user(self,user):
        token = user[1].json()["accessToken"]
        headers = {"Authorization": token}
        response_new_order = requests.post(f'{Urls.MAIN_URL}{Endpoints.CREATE_ORDER}', data=Ingredients.ingredients,headers=headers)
        response_get_order = requests.get(f'{Urls.MAIN_URL}{Endpoints.GET_ORDER}', headers=headers)
        assert response_new_order.json()["order"]["number"] == response_get_order.json()["orders"][0]["number"]

