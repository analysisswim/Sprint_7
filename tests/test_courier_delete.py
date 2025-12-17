import allure

from src.api.courier import CourierApi
from src.http_client import Http


@allure.feature("Courier")
class TestCourierDelete:

    @allure.title("Delete courier: without id returns 404")
    def test_delete_without_id(self):
        r = CourierApi(Http()).delete_without_id()
        assert r.status_code == 404
