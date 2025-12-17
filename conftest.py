import pytest

from src.http_client import Http
from src.api.courier import CourierApi
from src.api.orders import OrdersApi
from src.builders import build_courier, build_order_base


@pytest.fixture
def fresh_courier():
    """
    Сложная фикстура: создаёт курьера и гарантирует удаление (post-condition).
    """
    http = Http()
    api = CourierApi(http)

    payload = build_courier()
    create_r = api.create(payload)

    courier_id = None
    if create_r.status_code == 201:
        login_r = api.login(payload["login"], payload["password"])
        if login_r.status_code == 200 and "id" in login_r.json():
            courier_id = login_r.json()["id"]

    yield {
        "payload": payload,
        "create_response": create_r,
        "create_status": create_r.status_code,
        "id": courier_id,
    }

    if courier_id:
        api.delete(courier_id)


@pytest.fixture
def order_cleanup():
    """
    Сложная фикстура: регистрирует созданные track и отменяет их после теста.
    """
    http = Http()
    orders_api = OrdersApi(http)
    tracks = []

    def register(track: int):
        tracks.append(track)

    yield register

    for t in tracks:
        orders_api.cancel_by_track(t)


@pytest.fixture
def fresh_order(order_cleanup):
    """
    Сложная фикстура: создаёт заказ и гарантирует отмену.
    """
    http = Http()
    api = OrdersApi(http)

    r = api.create(build_order_base())
    track = None
    if r.status_code == 201:
        track = r.json().get("track")
        if track:
            order_cleanup(track)

    return {
        "create_response": r,
        "create_status": r.status_code,
        "track": track,
    }
