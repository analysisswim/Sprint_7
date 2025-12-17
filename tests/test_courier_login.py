import allure

from src.api.courier import CourierApi
from src.http_client import Http
from src.config import MSG_NOT_ENOUGH_DATA_LOGIN


@allure.feature("Courier")
class TestCourierLogin:

    @allure.title("Login requires both login and password")
    def test_login_requires_fields(self):
        api = CourierApi(Http())

        r1 = api.login(login="abc", password="")
        assert r1.status_code == 400, f"{r1.status_code} {r1.text}"
        assert r1.json().get("message") == MSG_NOT_ENOUGH_DATA_LOGIN

        r2 = api.login(login="", password="abc")
        assert r2.status_code == 400, f"{r2.status_code} {r2.text}"
        assert r2.json().get("message") == MSG_NOT_ENOUGH_DATA_LOGIN
