import pytest
import allure

from src.api.orders import OrdersApi
from src.builders import build_order_base
from src.http_client import Http


@allure.feature("Orders")
class TestOrdersCreate:
    @allure.title("Create order returns track for different color choices")
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order_track(self, order_cleanup, colors):
        api = OrdersApi(Http())
        payload = build_order_base()
        if colors is not None:
            payload["color"] = colors

        r = api.create(payload)
        assert r.status_code == 201

        body = r.json()
        assert "track" in body
        assert body["track"] is not None

        # постусловие
        order_cleanup.append(body["track"])
