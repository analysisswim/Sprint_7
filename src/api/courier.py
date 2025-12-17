import allure
from src.urls import COURIER_CREATE, COURIER_LOGIN
from src.http_client import Http


class CourierApi:
    def __init__(self, http: Http):
        self.http = http

    @allure.step("POST /courier - create courier")
    def create(self, payload: dict):
        return self.http.post(COURIER_CREATE, json=payload)

    @allure.step("POST /courier/login - login courier")
    def login_raw(self, payload: dict):
        return self.http.post(COURIER_LOGIN, json=payload)

    def login(self, login: str, password: str):
        return self.login_raw({"login": login, "password": password})

    @allure.step("DELETE /courier/{courier_id} - delete courier")
    def delete(self, courier_id: int):
        # Важно: в step НЕ используем {id}, чтобы не ловить KeyError
        return self.http.delete(f"{COURIER_CREATE}/{courier_id}")

    @allure.step("DELETE /courier - delete without id")
    def delete_without_id(self):
        # Удаление без айди должно вернуть 404 по тесту
        return self.http.delete(COURIER_CREATE)
