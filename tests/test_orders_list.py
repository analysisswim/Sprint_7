import allure

from src.api.orders import OrdersApi
from src.http_client import Http


@allure.feature("Orders")
class TestOrdersList:
    @allure.title("Orders list returns array in body.orders")
    def test_orders_list_has_orders_array(self):
        api = OrdersApi(Http())
        r = api.list()

        assert r.status_code == 200
        body = r.json()
        assert "orders" in body
        assert isinstance(body["orders"], list)
