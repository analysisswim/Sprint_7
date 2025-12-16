import allure

from src.api.orders import OrdersApi
from src.http_client import Http

MSG_NOT_ENOUGH_DATA = "Недостаточно данных для поиска"
MSG_ORDER_NOT_FOUND = "Заказ не найден"


@allure.feature("Orders")
class TestOrdersAccept:
    @allure.title("Accept order: success returns ok=true")
    def test_accept_success(self, fresh_courier, fresh_order):
        assert fresh_courier["create_status"] == 201
        assert fresh_order["create_status"] == 201

        courier_id = fresh_courier["id"]
        track = fresh_order["track"]
        assert courier_id is not None
        assert track is not None

        orders_api = OrdersApi(Http())

        get_r = orders_api.get_by_track(track)
        assert get_r.status_code == 200
        order_id = get_r.json()["order"]["id"]

        accept_r = orders_api.accept(order_id, courier_id)
        assert accept_r.status_code == 200
        assert accept_r.json() == {"ok": True}

    @allure.title("Accept order: missing courierId returns 400 and message")
    def test_accept_without_courier_id(self, fresh_order):
        assert fresh_order["create_status"] == 201
        track = fresh_order["track"]
        assert track is not None

        orders_api = OrdersApi(Http())
        get_r = orders_api.get_by_track(track)
        assert get_r.status_code == 200
        order_id = get_r.json()["order"]["id"]

        r = orders_api.accept_without_courier(order_id)
        assert r.status_code == 400
        assert r.json()["message"] == MSG_NOT_ENOUGH_DATA

    @allure.title("Accept order: non-existing order_id returns 404 and message")
    def test_accept_non_existing_order(self, fresh_courier):
        assert fresh_courier["create_status"] == 201
        courier_id = fresh_courier["id"]
        assert courier_id is not None

        orders_api = OrdersApi(Http())
        r = orders_api.accept(999999999, courier_id)

        assert r.status_code == 404
        assert r.json()["message"] == MSG_ORDER_NOT_FOUND
