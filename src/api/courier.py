from src.config import COURIER_CREATE, COURIER_LOGIN

class CourierApi:
    def __init__(self, http):
        self.http = http

    def create(self, payload: dict):
        return self.http.post(COURIER_CREATE, data=payload)

    def login(self, login: str, password: str):
        return self.http.post(COURIER_LOGIN, data={"login": login, "password": password})

    def delete(self, courier_id: int):
        # DELETE /courier/{id}
        return self.http.delete(f"{COURIER_CREATE}/{courier_id}")
