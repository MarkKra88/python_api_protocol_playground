Python API Protocol Playground
=============================

A collection of mini-projects exploring different types of API protocols using Python. Each module demonstrates how to interact with a real-world API (or create your own) using a specific protocol:

- REST
- GraphQL
- WebSocket
- SOAP
- gRPC
- MQTT

Project Goals
-------------
This repository is designed to:
- Integrate with external services using different protocols
- Compare synchronous vs. asynchronous API handling in Python
- Serve as a reusable learning or reference tool

Technologies Used
-----------------
- Python 3.10+
- requests / gql / websockets / zeep / grpcio / paho-mqtt
- Docker (optional for containerization)
- asyncio (for WebSocket handling)
- Protocol Buffers (for gRPC)

API Demos
---------
Each protocol is implemented as a standalone Python script/module under `/src`. Here’s a quick rundown:

Protocol   | Description                 | Live/Mock API Used
---------- | --------------------------- | ---------------------
REST       | Simple weather data fetcher | OpenWeatherMap
GraphQL    | Country data explorer       | Trevor Blades GraphQL API
WebSocket  | Real-time BTC/USDT price    | Binance WebSocket API
SOAP       | Number to Words converter   | DataAccess SOAP API
gRPC       | Fibonacci microservice demo | Custom gRPC service
MQTT       | Publish/Subscribe IoT mock  | Eclipse Mosquitto Broker


Setup Instructions
------
Copy `.env_template` to `.env` and fill in your API keys:
cp .env_template .env


License
------
This project is licensed under the MIT License.

Author
------
Mark Krawczak
GitHub: https://github.com/MarkKra88


