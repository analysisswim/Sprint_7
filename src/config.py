BASE_URL = "https://qa-scooter.praktikum-services.ru"
API_V1 = f"{BASE_URL}/api/v1"

# courier
COURIER_CREATE = f"{API_V1}/courier"
COURIER_LOGIN  = f"{API_V1}/courier/login"

# orders
ORDERS_CREATE = f"{API_V1}/orders"
ORDERS_LIST   = f"{API_V1}/orders"

# extra
ORDERS_CANCEL = f"{API_V1}/orders/cancel"   # PUT + params track=...
ORDERS_TRACK  = f"{API_V1}/orders/track"    # GET + params t=...
ORDERS_ACCEPT = f"{API_V1}/orders/accept"   # PUT /orders/accept/{orderId} + params courierId=...
