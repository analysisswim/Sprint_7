import pytest
from src.http_client import Http
from src.api.courier import CourierApi
from src.api.orders import OrdersApi
from src.builders import build_courier, build_order_base


@pytest.fixture
def http():
    return Http()


@pytest.fixture
def courier_api(http):
    return CourierApi(http)


@pytest.fixture
def orders_api(http):
    return OrdersApi(http)


@pytest.fixture
def fresh_courier(courier_api):
    """
    Создаёт курьера, возвращает dict: payload + id (если залогинился).
    После теста удаляет курьера, если id известен.
    """
    payload = build_courier()
    create_r = courier_api.create(payload)

    courier_id = None
    if create_r.status_code == 201:
        login_r = courier_api.login(payload["login"], payload["password"])
        if login_r.status_code == 200:
            courier_id = login_r.json().get("id")

    yield {"payload": payload, "id": courier_id, "create_status": create_r.status_code}

    if courier_id is not None:
        courier_api.delete(courier_id)


@pytest.fixture
def fresh_order(orders_api):
    """
    Создаёт заказ и возвращает track.
    После теста пытается отменить заказ по track (не критично, если отмена вернула ошибку).
    """
    payload = build_order_base()
    r = orders_api.create(payload)
    track = None
    if r.status_code == 201:
        track = r.json().get("track")

    yield {"track": track, "create_status": r.status_code}

    if track is not None:
        orders_api.cancel_by_track(track)
