from typing import Optional, Dict

class BaseGraphQLClient:
    """
    A base to client interact with GraphQL APIs.
    """

    def __init__(self,
                 endpoint: str,
                 headers: Optional[Dict[str, str]] = None) -> None:
        """
        Initialize the GraphQL client with an endpoint and optional headers.
        """
        self.endpoint = endpoint
        self.headers = headers or {}
        if "Content-Type" not in self.headers:
            self.headers["Content-Type"] = "application/json"