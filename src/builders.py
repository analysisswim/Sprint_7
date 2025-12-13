import random
import string
from datetime import date, timedelta

def _rand_letters(n: int = 10) -> str:
    alphabet = string.ascii_lowercase
    return "".join(random.choice(alphabet) for _ in range(n))

def build_courier():
    """Генерирует уникального курьера."""
    return {
        "login": _rand_letters(12),
        "password": _rand_letters(12),
        "firstName": _rand_letters(8),
    }

def build_order_base():
    """База заказа (без color). Дату даём на завтра, чтобы было стабильно."""
    return {
        "firstName": "Alex",
        "lastName": "Tester",
        "address": "Moscow, QA street, 7",
        "metroStation": 4,
        "phone": "+79991112233",
        "rentTime": 3,
        "deliveryDate": (date.today() + timedelta(days=1)).isoformat(),
        "comment": "api autotest sprint7",
    }
