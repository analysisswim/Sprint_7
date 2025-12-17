from src.config import BASE_URL

# Couriers
COURIER_CREATE = f"{BASE_URL}/api/v1/courier"
COURIER_LOGIN = f"{BASE_URL}/api/v1/courier/login"

# Orders (ИМЕНА ИМЕННО ТАКИЕ, как ждёт OrdersApi)
ORDERS = f"{BASE_URL}/api/v1/orders"                 # create + list
ORDERS_ACCEPT = f"{BASE_URL}/api/v1/orders/accept"   # accept by id
ORDERS_CANCEL = f"{BASE_URL}/api/v1/orders/cancel"   # cancel by track
ORDERS_TRACK = f"{BASE_URL}/api/v1/orders/track"     # get by track
