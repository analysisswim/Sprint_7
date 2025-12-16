import allure

from src.api.courier import CourierApi
from src.http_client import Http
from src.urls import COURIER_CREATE

MSG_COURIER_NOT_FOUND = "Курьера с таким id нет."


@allure.feature("Courier")
class TestCourierDelete:
    @allure.title("Delete courier: success returns 200 and ok=true")
    def test_delete_success(self, fresh_courier):
        assert fresh_courier["create_status"] == 201
        courier_id = fresh_courier["id"]
        assert courier_id is not None

        api = CourierApi(Http())
        r = api.delete(courier_id)

        assert r.status_code == 200
        assert r.json() == {"ok": True}

    @allure.title("Delete courier: non-existing id returns 404 and message")
    def test_delete_non_existing(self):
        api = CourierApi(Http())
        r = api.delete(999999999)

        assert r.status_code == 404
        assert r.json()["message"] == MSG_COURIER_NOT_FOUND

    @allure.title("Delete courier: without id in URL returns 404")
    def test_delete_without_id(self):
        http = Http()
        r = http.delete(COURIER_CREATE)  # DELETE /courier (без /{id})

        assert r.status_code == 404
