from typing import Dict, Optional, Any
from urllib.parse import urlencode
import requests
from src.core.utils import log_errors
import json
from urllib.request import Request, urlopen

class BaseRESTClient:

    """
    Initialize the REST client with a base URL, optional headers, and optional authentication token.
    """
    def __init__(self,
                 base_url: str,
                 headers: Optional[Dict[str, str]] = None,
                 auth_token: Optional[str] = None,
                 auth_type: str = "Bearer") -> None:
        self.base_url = base_url
        self.headers = headers or {}
        if auth_token:
            self.headers["Authorization"] = f"{auth_type} {auth_token}"

    """
        Build the full request URL by combining the base URL, endpoint, and any query parameter.
    """
    def build_url(self,
                  endpoint:str = "",
                  params: Optional[Dict[str, Any]] = None) ->str:
        url = f"{self.base_url.rstrip(f'/')}/{endpoint.lstrip('/')}"
        if params:
            query_string = urlencode(params)
            url = f"{url}?{query_string}"
        return url

    """
    Perform a GET request using 'urllib' library
    """
    @log_errors
    def get_with_urllib (self, url: str) -> dict:
        req = Request(url, headers= self.headers)
        with urlopen(req) as res:
            data = res.read().decode("utf-8")
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                return {"raw_data":data}

    """
    Perform a GET request using 'request' library
    """
    @log_errors
    def get_with_requests(self, url: str) -> dict:
        response = requests.get(url, headers=self.headers, allow_redirects=True, timeout=10)
        response.raise_for_status()
        return response.json()



    """
    Main GET method: tries 'requests' first, falls back to 'urllib' if needed.
    """
    @log_errors
    def get(self,
            endpoint: str = "",
            params: Optional[Dict[str, Any]] = None) -> dict:
        url = self.build_url(endpoint,params)

        try:
            return self.get_with_requests(url)
        except Exception as e:
            print("Primary request menthod failed. Retrying with backup (urllib)...")
        return self.get_with_urllib(url)


"""
Perform a test before pushing script.
"""

if __name__ == "__main__":

    client = BaseRESTClient(
        base_url="https://catfact.ninja/fact"
    )

    try:
        response = client.get()
        print("Success, raw response:")
        print(response.json()["fact"])
    except Exception as e:
        print("Request failed:")
        print(e)

