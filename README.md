# Kafka Clone

This project is a simplified Kafka clone that implements core Kafka-like functionalities, including accepting and responding to API requests (API Versions, Fetch API) and encoding/decoding messages using the Kafka wire protocol. The clone demonstrates handling the network protocol, event loops, TCP sockets, and more.

## Key Features

- **Port Binding**: The server binds to a port (default: `localhost:9092`) and listens for incoming client connections.
- **Correlation ID Handling**: Parses and responds with correlation IDs, ensuring requests and responses are properly tracked.
- **API Versions Parsing**: Parses API versions and responds with supported versions, sending error codes (`35`) for unsupported versions.
- **Serial and Concurrent Requests**: Handles multiple client requests both serially and concurrently using Python's `threading` module.
- **Kafka Wire Protocol**: Implements encoding and decoding messages following the Kafka wire protocol specification.

## Work in Progress

- **Message Consumption**: Currently working on implementing the Fetch API to handle message consumption requests from clients.
- **Enhanced Kafka Features**: Planning to expand support for additional Kafka features like the **Produce API**, message batching, and more robust error handling.

## Getting Started

### Prerequisites

Before running the server, ensure you have the following installed:

- **Python 3.x**

