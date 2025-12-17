import random
import string


def _rand_str(n=10):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(n))


def build_courier():
    return {
        "login": _rand_str(12),
        "password": _rand_str(12),
        "firstName": _rand_str(8),
    }


def build_order_base(colors=None):
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-12-31",
        "comment": "Saske, come back to Konoha",
    }
    # API ожидает поле "color" (список строк). Если None — не передаём вовсе.
    if colors is not None:
        payload["color"] = colors
    return payload
