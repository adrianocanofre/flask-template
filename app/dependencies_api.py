import requests


class DependencyApi:

    def __init__(self, base_url):
        self.base_url = base_url

    def _url(self, path):
        return self.base_url + path

    def healthcheck(self):
        try:
            response = requests.get(self._url('/api/healthcheck'))
            if response.status_code == 200:
                return True
        except:
            pass
        return False