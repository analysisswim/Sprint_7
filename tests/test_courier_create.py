import allure

from src.api.courier import CourierApi
from src.builders import build_courier
from src.http_client import Http
from src.config import MSG_NOT_ENOUGH_DATA_CREATE


@allure.feature("Courier")
class TestCourierCreate:

    @allure.title("Create courier: missing mandatory fields returns 400 and message")
    @allure.description("Обязательные поля по факту стенда: login, password.")
    def test_create_courier_missing_fields(self):
        api = CourierApi(Http())
        base = build_courier()

        for missing in ("login", "password"):
            payload = dict(base)
            payload.pop(missing)

            r = api.create(payload)

            assert r.status_code == 400, f"{r.status_code} {r.text}"
            assert r.json().get("message") == MSG_NOT_ENOUGH_DATA_CREATE

    @allure.title("Create courier: duplicate login returns 409 and message")
    def test_create_courier_duplicate(self, fresh_courier):
        # Первый курьер создаётся в фикстуре fresh_courier
        payload = fresh_courier["payload"]

        api = CourierApi(Http())
        r = api.create(payload)

        assert r.status_code == 409, f"Unexpected {r.status_code}, body: {r.text}"
        # сообщение у стенда часто именно такое:
        assert "message" in r.json()
