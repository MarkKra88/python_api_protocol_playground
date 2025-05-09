from typing import Optional, Dict, Any
from src.core.utils import log_errors
import requests
import json

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
            "variables": variables if variables is not None else {}
        }


        response = requests.post(
            self.endpoint,
            headers = self.headers,
            json = payload,
            timeout = 10
        )
        response.raise_for_status()
        return response.json()

"""
Perform a test before pushing script.
"""

if __name__ == "__main__":
    print("Use this format for input:")
    print("Headers:      key=value&key2=value2")
    print("Variables:    key=value&key2=value2")
    print("Query:        Multiline GraphQL query")

    endpoint = input("Enter GraphQL endpoint: ").strip()

    headers_input =input("Enter headers (or leave blank): ").strip()

    headers = {}

    if headers_input:
        for pair in headers_input.split("&"):
            if "=" in pair:
                key, value = pair.strip().split("=",1)
                headers[key.strip()] = value.strip()

    query_lines = []
    print("Paste your GraphQL query(end with an empty line):")
    while True:
        line = input()
        if line == "":
            break
        query_lines.append(line)
    query_string = "\n".join(query_lines)

    variables_input = input("Enter variables (or leave blank): ").strip()
    variables = (
        dict(item.split("=",1) for item in variables_input.split("&"))
        if variables_input else None
    )

    client = BaseGraphQLClient(endpoint=endpoint, headers=headers)

    query_string_sec = 'query { country(code: "PL") { name capital currency languages { name } } }'
    try:
        result = client.query(query=query_string, variables=variables)
        print("GraphQL Response:")
        print(json.dumps(result,indent=2))
    except Exception as e:
        print(f"GraphQL request failed: {e}")