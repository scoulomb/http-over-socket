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


def request_as_string(request: Request, hostname: str) -> str:
    request_lines = [f"{request.method} {request.path} HTTP/1.1",
                     f"Host: {hostname}",
                     *request.headers,
                     HEADER_SEPARATOR.decode(),
                     ]  # empty body?

    request = "\r\n".join(request_lines)
    return request


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

    hostname = "www.google.com"
    port = 443
    connection = Connection(hostname, port)
    request = Request("GET", "/", ["Accept: */*"])
    response = send(connection, request)
    print(response)


def send(connection: Connection, request: Request) -> str:
    buffer_size = 1024

    request_str: str = request_as_string(request, connection.hostname)
    print(request_str)
    https_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    # TCP / IPv4
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as raw_socket:
        s = https_context.wrap_socket(raw_socket, server_hostname=connection.hostname)
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
        s.send(request_str.encode())
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

# our client managed content-length only but some server retruns a Transfer-Encoding with the size of the chunk
# https://tools.ietf.org/html/rfc7230#section-3.3.2

# use www.google.com to not have -L