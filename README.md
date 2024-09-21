# Kafka_implementation
Building a custom Kafka broker capable of serving basic requests, exploring TCP servers and the Kafka wire protocol along the way.

--I implemented a TCP server that listens on port 9092, utilizing TCP as the underlying protocol for communication, similar to well-known protocols like HTTP and SSH.
This server facilitates interaction between Kafka clients and brokers. As part of the implementation, I hardcoded the correlation ID to a fixed number in the response while also parsing the correlation ID from incoming requests to ensure consistency. 
Additionally, I parsed the api_version field from requests and implemented logic to respond with an error if the version is unsupported. 
Finally, I developed the response body for the APIVersions request, completing the server's basic functionality.

Currently working on Serial Requests .






