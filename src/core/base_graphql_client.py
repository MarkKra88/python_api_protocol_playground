from typing import Optional, Dict, Any
from src.core.utils import log_errors
import requests

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

    @log_errors
    def query(self,
              query: str,
              variables: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Execute a GraphQL query with optional variables.
        Returns the JSON response as a dictionary.
        """
        payload =  {
            "query": query,
            "variables": variables or {}
        }

        response = requests.post(
            self.endpoint,
            headers = self.endpoint,
            json = payload,
            timeout = 10
        )
        response.raise_for_status()
        return response.json()