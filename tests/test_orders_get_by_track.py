import allure

from src.api.orders import OrdersApi
from src.http_client import Http

MSG_NOT_ENOUGH_DATA = "Недостаточно данных для поиска"
MSG_ORDER_NOT_FOUND = "Заказ не найден"


@allure.feature("Orders")
class TestOrdersGetByTrack:
    @allure.title("Get order by track: success returns 200 and order object")
    def test_get_by_track_success(self, fresh_order):
        assert fresh_order["create_status"] == 201
        track = fresh_order["track"]
        assert track is not None

        api = OrdersApi(Http())
        r = api.get_by_track(track)

        assert r.status_code == 200
        assert "order" in r.json()
        assert "id" in r.json()["order"]

    @allure.title("Get order by track: missing track returns 400 and message")
    def test_get_by_track_without_track(self):
        api = OrdersApi(Http())
        r = api.get_by_track_raw(params={})  # без t

        assert r.status_code == 400
        assert r.json()["message"] == MSG_NOT_ENOUGH_DATA

    @allure.title("Get order by track: non-existing track returns 404 and message")
    def test_get_by_track_non_existing(self):
        api = OrdersApi(Http())
        r = api.get_by_track(999999999)

        assert r.status_code == 404
        assert r.json()["message"] == MSG_ORDER_NOT_FOUND
