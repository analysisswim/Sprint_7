import allure
from src.builders import build_order_base


@allure.feature("Orders")
class TestOrdersAccept:

    @allure.title("Accept order: success returns ok=true")
    def test_accept_success(self, orders_api, courier_api, fresh_courier):
        # courier
        courier_id = fresh_courier["id"]
        assert courier_id is not None

        # create order
        create_r = orders_api.create(build_order_base())
        assert create_r.status_code == 201
        track = create_r.json()["track"]

        # get order_id by track
        get_r = orders_api.get_by_track(track)
        assert get_r.status_code == 200
        order_id = get_r.json()["order"]["id"]

        # accept
        accept_r = orders_api.accept(order_id=order_id, courier_id=courier_id)
        assert accept_r.status_code == 200
        assert accept_r.json() == {"ok": True}

        # cleanup order
        orders_api.cancel_by_track(track)

    @allure.title("Accept order: missing courierId returns error")
    def test_accept_without_courier_id(self, http, fresh_order):
        track = fresh_order["track"]
        assert track is not None

        get_r = http.get("https://qa-scooter.praktikum-services.ru/api/v1/orders/track", params={"t": track})
        order_id = get_r.json()["order"]["id"]

        r = http.put(f"https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}")  # без courierId
        assert r.status_code in (400, 404)
        assert "message" in r.json()

    @allure.title("Accept order: invalid courierId returns error")
    def test_accept_with_invalid_courier_id(self, orders_api, fresh_order):
        track = fresh_order["track"]
        assert track is not None

        get_r = orders_api.get_by_track(track)
        order_id = get_r.json()["order"]["id"]

        r = orders_api.accept(order_id=order_id, courier_id=999999999)
        assert r.status_code in (400, 404)
        assert "message" in r.json()
