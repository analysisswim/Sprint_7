import allure

from src.urls import COURIER_CREATE, COURIER_LOGIN, COURIER_DELETE


class CourierApi:
    def __init__(self, http):
        self.http = http

    @allure.step("POST /courier — create courier")
    def create(self, payload: dict):
        return self.http.post(COURIER_CREATE, json=payload)

    @allure.step("POST /courier/login — login courier")
    def login(self, login: str, password: str):
        return self.http.post(COURIER_LOGIN, json={"login": login, "password": password})

    @allure.step("POST /courier/login — login courier (raw payload)")
    def login_raw(self, payload: dict):
        return self.http.post(COURIER_LOGIN, json=payload)

    @allure.step("DELETE /courier/{courier_id} — delete courier")
    def delete(self, courier_id: int):
        return self.http.delete(f"{COURIER_DELETE}{courier_id}")
