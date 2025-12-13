import allure
from src.builders import build_courier


@allure.feature("Courier")
class TestCourierCreate:

    @allure.title("Create courier: success returns 201 and ok=true")
    def test_create_courier_success(self, courier_api):
        payload = build_courier()
        r = courier_api.create(payload)

        assert r.status_code == 201
        assert r.json() == {"ok": True}

        # cleanup
        login_r = courier_api.login(payload["login"], payload["password"])
        courier_id = login_r.json()["id"]
        courier_api.delete(courier_id)

    @allure.title("Create courier: cannot create duplicates")
    def test_create_courier_duplicate(self, courier_api):
        payload = build_courier()

        r1 = courier_api.create(payload)
        assert r1.status_code == 201

        r2 = courier_api.create(payload)
        assert r2.status_code == 409
        assert "message" in r2.json()

        # cleanup
        login_r = courier_api.login(payload["login"], payload["password"])
        courier_api.delete(login_r.json()["id"])

    @allure.title("Create courier: missing mandatory fields returns error")
    def test_create_courier_missing_fields(self, courier_api):
        r = courier_api.create({"login": "only_login"})
        assert r.status_code == 400
        assert "message" in r.json()
