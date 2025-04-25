from typing import Dict, Optional, Any
from urllib.parse import urlencode
import requests
from src.core.utils import log_errors

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
    Perform a GET request to the given endpoint with optional query parameters.
    Returns the raw HTML repsonse object(status, headers, content).
    """

    @log_errors
    def get(self,
            endpoint: str = "",
            params: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = self.build_url(endpoint,params)
        response = requests.get(url,headers=self.headers)
        response.raise_for_status() # This triggers @log_error only on failure
        return response


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

