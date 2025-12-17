import allure
from src.http_client import Http
from src.urls import COURIER_CREATE, COURIER_LOGIN


class CourierApi:
    def __init__(self, http: Http):
        self.http = http

    @allure.step("POST /courier — create courier")
    def create(self, payload: dict):
        return self.http.post(COURIER_CREATE, json=payload)

    @allure.step("POST /courier/login — login (raw payload)")
    def login_raw(self, payload: dict):
        return self.http.post(COURIER_LOGIN, json=payload)

    @allure.step("POST /courier/login — login")
    def login(self, login: str, password: str):
        return self.login_raw({"login": login, "password": password})

    @allure.step("DELETE /courier/{courier_id} — delete courier")
    def delete(self, courier_id: int):
        return self.http.delete(f"{COURIER_CREATE}/{courier_id}")

    @allure.step("DELETE /courier — delete without id")
    def delete_without_id(self):
        return self.http.delete(COURIER_CREATE)
