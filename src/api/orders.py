import allure
from typing import Optional, Dict, Any

from src.urls import (
    ORDERS_CREATE,
    ORDERS_LIST,
    ORDERS_TRACK,
    ORDERS_ACCEPT,
    ORDERS_CANCEL,
)


class OrdersApi:
    def __init__(self, http):
        self.http = http

    @allure.step("POST /orders — create order")
    def create(self, payload: Dict[str, Any]):
        return self.http.post(ORDERS_CREATE, json=payload)

    @allure.step("GET /orders — list orders")
    def list(self, params: Optional[Dict[str, Any]] = None):
        return self.http.get(ORDERS_LIST, params=params)

    @allure.step("GET /orders/track?t={track} — get order by track")
    def get_by_track(self, track: int):
        return self.http.get(ORDERS_TRACK, params={"t": track})

    @allure.step("GET /orders/track — get order by track (raw params)")
    def get_by_track_raw(self, params: Optional[Dict[str, Any]] = None):
        return self.http.get(ORDERS_TRACK, params=params)

    @allure.step("PUT /orders/accept/{order_id}?courierId={courier_id} — accept order")
    def accept(self, order_id: int, courier_id: int):
        return self.http.put(f"{ORDERS_ACCEPT}{order_id}", params={"courierId": courier_id})

    @allure.step("PUT /orders/accept/{order_id} — accept order without courierId")
    def accept_without_courier(self, order_id: int):
        return self.http.put(f"{ORDERS_ACCEPT}{order_id}")

    @allure.step("PUT /orders/cancel — cancel order by track")
    def cancel_by_track(self, track: int):
        return self.http.put(ORDERS_CANCEL, json={"track": track})
