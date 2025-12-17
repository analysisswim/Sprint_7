import allure
from typing import Optional, Dict, Any

from src.urls import ORDERS, ORDERS_ACCEPT, ORDERS_CANCEL, ORDERS_TRACK
from src.http_client import Http


class OrdersApi:
    def __init__(self, http: Http):
        self.http = http

    @allure.step("POST /orders - create order")
    def create(self, payload: Dict[str, Any]):
        return self.http.post(ORDERS, json=payload)

    @allure.step("GET /orders - list orders")
    def list(self, params: Optional[Dict[str, Any]] = None):
        return self.http.get(ORDERS, params=params)

    @allure.step("GET /orders/track - get order by track")
    def get_by_track(self, track: int):
        return self.http.get(ORDERS_TRACK, params={"t": track})

    @allure.step("GET /orders/track - get order by track (raw params)")
    def get_by_track_raw(self, params: Dict[str, Any]):
        return self.http.get(ORDERS_TRACK, params=params)

    @allure.step("PUT /orders/accept/{order_id} - accept order by courier")
    def accept(self, order_id: int, courier_id: int):
        return self.http.put(f"{ORDERS_ACCEPT}/{order_id}", params={"courierId": courier_id})

    @allure.step("PUT /orders/cancel - cancel order by track")
    def cancel_by_track(self, track: int):
        return self.http.put(ORDERS_CANCEL, params={"track": track})
