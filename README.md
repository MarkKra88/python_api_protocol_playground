Python API Protocol Playground
=============================

This project is created as a playground for testing various API protocols using Python. It focuses on building minimal but modular backend code using best practices (SOLID principles, clean structure, reusable base classes, and CLI-based interaction instead of UI). It’s designed more for backend understanding and API behavior exploration than production deployment.


- REST ✅
- GraphQL ✅
- WebSocket ⏳
- SOAP ⏳
- gRPC ⏳
- MQTT ⏳

Project Goals
-------------
This repository is designed to:
- Integrate with external services using different protocols
- Create reusable 'BaseClient' structure with pluggable endpoints
- Compare synchronous vs. asynchronous API handling in Python
- Use CLI-driven development to simulate frontend integration flow
- Serve as a reusable learning or reference tool
- Log structured errors using decorators for debugging and future dashboarding

Technologies Used
-----------------
- Python 3.10+
- `requests` (REST/GraphQL)
- `dotenv` (for local environment handling)
- Built-in modules only unless needed per protocol


PROTOCOLS PLANNED
---------
Each protocol is implemented as a standalone Python script/module under `/src`. Here’s a quick rundown:

| Protocol  | Description | 
|-----------|-------------|
| REST      | Done        | 
| GraphQL   | Done        | 
| WebSocket | Planned     | 
| SOAP      | Planned     | 
| gRPC      | Planned     | 
| MQTT      | Planned     | 



## CURRENT STRUCTURE

- `src/core/` – Shared base clients (`BaseRESTClient`, `BaseGraphQLClient`), error logging decorators
- `src/rest_api/` – Specific implementations, e.g. EPC API
- `src/graphql/` – Optional subclients or schema-specific logic
- `.env_template` – Template for managing sensitive data
- `.gitignore` – Excludes venv, `.env`, logs, etc.

## TESTING & USAGE

- Each protocol can be run standalone via `if __name__ == "__main__"` section in the base client

License
------
This project is licensed under the MIT License.

Author
------
Mark Krawczak
GitHub: https://github.com/MarkKra88


