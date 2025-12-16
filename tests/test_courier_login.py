import allure

from src.api.courier import CourierApi
from src.http_client import Http

MSG_NOT_ENOUGH_DATA_LOGIN = "Недостаточно данных для входа"
MSG_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"


@allure.feature("Courier")
class TestCourierLogin:
    @allure.title("Login courier: success returns 200 and id")
    def test_login_success(self, fresh_courier):
        assert fresh_courier["create_status"] == 201
        payload = fresh_courier["payload"]

        api = CourierApi(Http())
        r = api.login(payload["login"], payload["password"])

        assert r.status_code == 200
        assert "id" in r.json()

    @allure.title("Login requires both login and password")
    def test_login_requires_fields(self):
        api = CourierApi(Http())

        r1 = api.login_raw({"login": "abc"})
        assert r1.status_code == 400
        assert r1.json()["message"] == MSG_NOT_ENOUGH_DATA_LOGIN

        r2 = api.login_raw({"password": "123"})
        assert r2.status_code == 400
        assert r2.json()["message"] == MSG_NOT_ENOUGH_DATA_LOGIN

    @allure.title("Login with wrong credentials returns 404 and message")
    def test_login_wrong_credentials(self):
        api = CourierApi(Http())
        r = api.login("no_such_login_123", "no_such_password_123")

        assert r.status_code == 404
        assert r.json()["message"] == MSG_ACCOUNT_NOT_FOUND
