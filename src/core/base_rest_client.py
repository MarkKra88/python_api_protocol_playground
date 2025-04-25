from typing import Dict, Optional

class BaseRESTclient:
    def __init__(self,
                 base_url: str,
                 headers: Optional[Dict[str, str]] = None,
                 auth_token: Optional[str] = None,
                 auth_type: str = "Bearer") -> None:
        self.base_url = base_url
        self.headers = headers or {}
        if auth_token:
            self.headers["Authorization"] = f"{auth_type} {auth_token}"
