from typing import Any

import requests
from requests import Response


class BaseApi:

    def __init__(self) -> None:

        self.headers = {
            'Content-Type': 'application/json'
        }

    @staticmethod
    def request(method: str, url: str, **kwargs: Any) -> Response:
        response = requests.request(method=method, url=url, **kwargs)
        return response
