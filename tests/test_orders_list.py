import allure


@allure.feature("Orders")
class TestOrdersList:

    @allure.title("Orders list returns array in body.orders")
    def test_orders_list_has_orders_array(self, orders_api):
        r = orders_api.list()
        assert r.status_code == 200

        body = r.json()
        assert "orders" in body
        assert isinstance(body["orders"], list)
