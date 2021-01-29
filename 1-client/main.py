import socket
import ssl
from dataclasses import dataclass
from typing import List, Optional

HEADER_SEPARATOR = b"\r\n\r\n"


@dataclass
class Request:
    method: str
    path: str
    headers: List[str]
    body: Optional[str] = None
    timeout_seconds: int = 10


def request_as_string(request: Request, hostname: str, port: int) -> str:
    user_request_headers = [*request.headers]
    if len(user_request_headers) > 0:
        user_header_str = "\r\n".join(user_request_headers) + "\r\n"
    else:
        user_header_str = ""

    if request.body is None:
        request.body = ""

    # To build the request_str with body message I used as a model:
    # s.send(
    #    b'POST /api/v1/namespaces/default/pods HTTP/1.1\r\nHost: 127.0.0.1:9515\r\nContent-Type: application/json\r\nContent-Length: 155\r\n\r\n{"apiVersion":"v1","kind":"Pod","metadata":{"name":"nginx1"},"spec":{"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80}]}]}}')
    # based on https://stackoverflow.com/questions/45695168/send-raw-post-request-using-socket (see README, Example of simple usage using Kubernetes API)
    request_str = f'{request.method} {request.path} HTTP/1.1\r\n' \
                  f'Host: {hostname}:{port}\r\n' \
                  f'Content-Type: application/json\r\n' \
                  f'{user_header_str}' \
                  f'Content-Length: {len(request.body)}\r\n' \
                  f'\r\n' \
                  f'{request.body}'

    # Adding extra '\r\n' here, will make the client send 2 messages. Server will send a 400 (like kubectl proxy) and some will close the connection

    return request_str


@dataclass
class Connection:
    hostname: str
    port: int
    timeout_seconds: int = 20
    protocol: str = "https"


def main():
    # we have to add host header for routing (cloud run name mapping, kubernetes ingress, openshift router...)
    # Example:
    # curl -k -L -H "Host: " https://attestationcovid.site -v -> failing
    # whereas by default working as curl add the Host header marching the `hostname`

    hostname = "attestationcovid.site"
    port = 443
    connection = Connection(hostname, port)
    request = Request("GET", "/", ["Accept: */*"])
    response = send(connection, request)
    print(response)

    hostname = "attestationcovid.site"
    port = 80
    connection = Connection(hostname, port, protocol="http")
    request = Request("GET", "/", ["Accept: */*"])
    response = send(connection, request)
    print(response)


def send(connection: Connection, request: Request) -> str:
    buffer_size = 1024

    request_str: str = request_as_string(request, connection.hostname, connection.port)
    print(request_str)

    # TCP / IPv4
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as raw_socket:
        if connection.protocol == "https":
            https_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            s = https_context.wrap_socket(raw_socket, server_hostname=connection.hostname)
        else:
            s = raw_socket
        s.settimeout(connection.timeout_seconds)

        try:
            s.connect((connection.hostname, connection.port))
        except socket.gaierror as e:
            message = f"Connection failed with socket error {e.errno} "  # dir(e) to check attribute
            raise Exception(message) from e
        except socket.timeout as e:
            message = f"Connection timeout after {connection.timeout_seconds} seconds"
            raise Exception(message) from e

        print(f"connection established with host {connection.hostname}")

        s.settimeout(request.timeout_seconds)
        s.send(bytes(request_str, "utf-8"))

        print("request sent")

        headers_finished: bool = False

        response_bytes: bytes = b""
        body_len: Optional[int] = None

        while True:
            buffer_byte: bytes = s.recv(buffer_size)
            response_bytes += buffer_byte
            if len(buffer_byte) == 0:
                break

            # detect end of header
            if HEADER_SEPARATOR in response_bytes:
                headers_finished = True

            if headers_finished:
                print("headers finished")
                headers = response_bytes.split(HEADER_SEPARATOR)[0]
                if b"Content-Length:" in headers:
                    body_len = int(response_bytes.split(b"Content-Length: ")[1].split(b"\r\n")[0].decode())
                else:
                    print("no body")
                    break  # case we do not have body and no Content-Length

            if body_len is not None:  # We can have no body if Content-Length = 0
                body = response_bytes.split(HEADER_SEPARATOR)[1]
                if len(body) == body_len:
                    break

        return response_bytes.decode()  # decode(errors="ignore")


if __name__ == "__main__":
    main()

# use www.google.com to not have -L
