import pytest

from src.api.courier import CourierApi
from src.api.orders import OrdersApi
from src.builders import build_courier, build_order_base
from src.http_client import Http


@pytest.fixture
def courier_cleanup():
    """Постусловие: удалить всех курьеров, id которых добавят в список."""
    courier_ids: list[int] = []
    yield courier_ids

    api = CourierApi(Http())
    for cid in courier_ids:
        # если уже удалили в тесте — в уборке 404 не критично
        api.delete(cid)


@pytest.fixture
def order_cleanup():
    """Постусловие: отменить все заказы по треку, добавленные в список."""
    tracks: list[int] = []
    yield tracks

    api = OrdersApi(Http())
    for t in tracks:
        api.cancel_by_track(t)


@pytest.fixture
def fresh_courier(courier_cleanup):
    """Предусловие: создать курьера. Постусловие: удалить."""
    api = CourierApi(Http())
    payload = build_courier()
    create_r = api.create(payload)

    courier_id = None
    if create_r.status_code == 201:
        login_r = api.login(payload["login"], payload["password"])
        if login_r.status_code == 200 and "id" in login_r.json():
            courier_id = login_r.json()["id"]
            courier_cleanup.append(courier_id)

    return {
        "payload": payload,
        "create_status": create_r.status_code,
        "id": courier_id,
        "response": create_r,
    }


@pytest.fixture
def fresh_order(order_cleanup):
    """Предусловие: создать заказ. Постусловие: отменить заказ по треку."""
    api = OrdersApi(Http())
    create_r = api.create(build_order_base())

    track = None
    if create_r.status_code == 201 and "track" in create_r.json():
        track = create_r.json()["track"]
        order_cleanup.append(track)

    return {
        "track": track,
        "create_status": create_r.status_code,
        "response": create_r,
    }
