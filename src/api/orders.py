from src.config import (
    ORDERS_CREATE, ORDERS_LIST,
    ORDERS_CANCEL, ORDERS_TRACK, ORDERS_ACCEPT
)

class OrdersApi:
    def __init__(self, http):
        self.http = http

    def create(self, payload: dict):
        # у заказов обычно принимается json
        return self.http.post(ORDERS_CREATE, json=payload)

    def list(self):
        return self.http.get(ORDERS_LIST)

    def cancel_by_track(self, track: int):
        # важно: track в params, а не в body
        return self.http.put(ORDERS_CANCEL, params={"track": track})

    def get_by_track(self, track: int):
        # важно: t в params
        return self.http.get(ORDERS_TRACK, params={"t": track})

    def accept(self, order_id: int, courier_id: int):
        # важно: courierId в params
        return self.http.put(f"{ORDERS_ACCEPT}/{order_id}", params={"courierId": courier_id})
