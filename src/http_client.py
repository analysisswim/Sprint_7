import requests

class Http:
    """Тонкая обёртка над requests.Session для единообразия вызовов."""
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, **kwargs):
        return self.session.get(url, **kwargs)

    def post(self, url, **kwargs):
        return self.session.post(url, **kwargs)

    def put(self, url, **kwargs):
        return self.session.put(url, **kwargs)

    def patch(self, url, **kwargs):
        return self.session.patch(url, **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete(url, **kwargs)
