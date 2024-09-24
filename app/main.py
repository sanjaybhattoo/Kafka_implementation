import socket


def main():
    print("Logs from your program will appear here!")

    
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    client_socket, _ = server.accept()

    
    req = client_socket.recv(1024)

    # Extract API Key, API Version, and Correlation ID from the request
    api_key = int.from_bytes(req[4:6], byteorder='big')
    api_ver = int.from_bytes(req[6:8], byteorder='big')
    correlation_id = int.from_bytes(req[8:12], byteorder='big')

    # Set up the error code and check if the API key is 18 (APIVersions)
    err_code = 0  # No error

    # Ensure we're working with API_VERSIONS (API Key 18)
    if api_key != 18:
        err_code = 35  # Unsupported version error (if not API key 18)

    
    valid_versions = [0, 1, 2, 3, 4]
    if api_ver not in valid_versions:
        err_code = 35
    # Define the min and max versions for API key 18
    min_version = 0
    max_version = 4  # Max version for API key 18 is at least 4

    # Build the API version response (for API key 18)
    api_version_resp = (
        api_key.to_bytes(2)  # API Key (18)
        + min_version.to_bytes(2)  # Min Version (0)
        + max_version.to_bytes(2)  # Max Version (4)
    )

    tag_buffer =b"\x00"
    throttle_time = 0
    # Build the response body (error code + API version data)
    response_body = (
        err_code.to_bytes(2, byteorder='big')  # Error code (No error)
        + int(2).to_bytes(1, byteorder='big')  # Number of API versions (1 for APIVersions)
        + api_version_resp  # API versions data (for API key 18)
        + tag_buffer
        + throttle_time.to_bytes(4)
        + tag_buffer
    )
    resp_head = correlation_id.to_bytes(4)
    # Calculate the length of the response (excluding the first 4 bytes for length itself)
    response_len = len(response_body) + len(resp_head)  # 4 bytes for the correlation ID

    # Build the complete response (message length + correlation ID + response body)
    response = (
        response_len.to_bytes(4, byteorder='big', signed=False)  # Message length (unsigned)
        + correlation_id.to_bytes(4, byteorder='big', signed=False)  # Correlation ID (unsigned)
        + response_body  # Response body
    )

    # Send the response back to the client
    client_socket.sendall(response)

    # Close the connection
    client_socket.close()
    server.close()


if __name__ == "__main__":
    main()
