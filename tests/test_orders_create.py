import pytest
import allure
from src.builders import build_order_base


@allure.feature("Orders")
class TestOrdersCreate:

    @allure.title("Create order returns track for different color choices")
    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None
    ])
    def test_create_order_track(self, orders_api, colors):
        payload = build_order_base()
        if colors is not None:
            payload["color"] = colors

        r = orders_api.create(payload)
        assert r.status_code == 201

        body = r.json()
        assert "track" in body
        assert body["track"] is not None

        # cleanup
        orders_api.cancel_by_track(body["track"])
