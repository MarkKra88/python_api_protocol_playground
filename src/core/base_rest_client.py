from typing import Dict, Optional, Any
from urllib.parse import urlencode

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