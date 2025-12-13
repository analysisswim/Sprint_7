import allure
from src.config import COURIER_CREATE


@allure.feature("Courier")
class TestCourierDelete:

    @allure.title("Delete courier: success returns ok=true")
    def test_delete_success(self, courier_api, fresh_courier):
        courier_id = fresh_courier["id"]
        assert courier_id is not None

        r = courier_api.delete(courier_id)
        assert r.status_code == 200
        assert r.json() == {"ok": True}

    @allure.title("Delete courier: without id returns error")
    def test_delete_without_id(self, http):
        r = http.delete(COURIER_CREATE)  # DELETE /courier (без /{id})
        assert r.status_code in (400, 404, 405)

    @allure.title("Delete courier: non-existing id returns error")
    def test_delete_non_existing_id(self, courier_api):
        r = courier_api.delete(999999999)
        assert r.status_code in (400, 404)
        assert "message" in r.json()
