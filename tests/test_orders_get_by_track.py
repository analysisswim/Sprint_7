import allure


@allure.feature("Orders")
class TestOrdersGetByTrack:

    @allure.title("Get order by track returns order object")
    def test_get_by_track_success(self, orders_api, fresh_order):
        track = fresh_order["track"]
        assert track is not None

        r = orders_api.get_by_track(track)
        assert r.status_code == 200
        assert "order" in r.json()

    @allure.title("Get order by track: without track returns error")
    def test_get_by_track_without_param(self, http):
        # GET /orders/track без params
        r = http.get("https://qa-scooter.praktikum-services.ru/api/v1/orders/track")
        assert r.status_code in (400, 404)
        assert "message" in r.json()

    @allure.title("Get order by track: non-existing track returns error")
    def test_get_by_track_non_existing(self, orders_api):
        r = orders_api.get_by_track(999999999)
        assert r.status_code in (400, 404)
        assert "message" in r.json()
