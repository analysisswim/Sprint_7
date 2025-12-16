import allure

from src.api.courier import CourierApi
from src.builders import build_courier
from src.http_client import Http

MSG_NOT_ENOUGH_DATA_CREATE = "Недостаточно данных для создания учетной записи"
MSG_LOGIN_ALREADY_USED = "Этот логин уже используется"


@allure.feature("Courier")
class TestCourierCreate:
    @allure.title("Create courier: success returns 201 and ok=true")
    def test_create_courier_success(self, courier_cleanup):
        api = CourierApi(Http())
        payload = build_courier()

        r = api.create(payload)

        assert r.status_code == 201
        assert r.json() == {"ok": True}

        # постусловие: удалить курьера
        login_r = api.login(payload["login"], payload["password"])
        assert login_r.status_code == 200
        courier_id = login_r.json()["id"]
        courier_cleanup.append(courier_id)

    @allure.title("Create courier: duplicate login returns 409 and message")
    def test_create_courier_duplicate(self, fresh_courier):
        assert fresh_courier["create_status"] == 201

        api = CourierApi(Http())
        payload = fresh_courier["payload"]

        r = api.create(payload)

        assert r.status_code == 409
        assert r.json()["message"] == MSG_LOGIN_ALREADY_USED

    @allure.title("Create courier: missing mandatory fields returns 400 and message")
    @allure.description("Обязательные поля: login, password, firstName.")
    def test_create_courier_missing_fields(self):
        api = CourierApi(Http())
        base = build_courier()

        for missing in ("login", "password", "firstName"):
            payload = dict(base)
            payload.pop(missing)

            r = api.create(payload)

            assert r.status_code == 400
            assert r.json()["message"] == MSG_NOT_ENOUGH_DATA_CREATE
