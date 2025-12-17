import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


class Http:
    def __init__(self, timeout: int = 20):
        self.timeout = timeout
        self.session = requests.Session()

        retry = Retry(
            total=3,
            connect=3,
            read=3,
            backoff_factor=0.5,
            status_forcelist=(502, 503, 504),
            allowed_methods=("GET", "POST", "PUT", "DELETE"),
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def get(self, url, params=None, timeout=None):
        return self.session.get(url, params=params, timeout=timeout or self.timeout)

    def post(self, url, json=None, data=None, params=None, timeout=None):
        return self.session.post(url, json=json, data=data, params=params, timeout=timeout or self.timeout)

    def put(self, url, json=None, data=None, params=None, timeout=None):
        return self.session.put(url, json=json, data=data, params=params, timeout=timeout or self.timeout)

    def delete(self, url, timeout=None):
        return self.session.delete(url, timeout=timeout or self.timeout)
