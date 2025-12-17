import allure

from src.http_client import Http
from src.api.orders import OrdersApi
from src.builders import build_order_base
from src.config import MSG_ORDER_ID_NOT_EXISTS


class TestOrdersAccept:
    @allure.title("Accept order: success returns ok=true")
    def test_accept_success(self, fresh_courier, fresh_order):
        courier_id = fresh_courier["id"]

        api = OrdersApi(Http())

        # get order_id by track
        track = fresh_order["track"]
        get_r = api.get_by_track(track)
        assert get_r.status_code == 200

        order_id = get_r.json()["order"]["id"]

        accept_r = api.accept(order_id, courier_id)
        assert accept_r.status_code == 200
        assert accept_r.json() == {"ok": True}

    @allure.title("Accept order: non-existing order_id returns 404 and message")
    def test_accept_non_existing_order(self, fresh_courier):
        courier_id = fresh_courier["id"]

        api = OrdersApi(Http())
        r = api.accept(999999999, courier_id)

        assert r.status_code == 404
        assert r.json()["message"] == MSG_ORDER_ID_NOT_EXISTS
