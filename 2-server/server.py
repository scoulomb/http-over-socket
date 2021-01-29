import argparse
import ipaddress
import socket
from argparse import Namespace

HEADER_SEPARATOR = b"\r\n\r\n"
HEADER_SEPARATOR_STR = "\r\n\r\n"


def _read_cli_arguments() -> Namespace:
    parser = argparse.ArgumentParser(
        description="HTTP 2-server over Socket")

    parser.add_argument(
        "--ip",
        type=str,
        default="0.0.0.0")

    parser.add_argument(
        "--port",
        type=int,
        default=8080
    )

    return parser.parse_args()


def no_content() -> str:
    return f'HTTP/1.1 204 NO CONTENT\r\n' \
           f'Content-Type: application/json\r\n' \
           f'\r\n'


# this is the exact same code as in client when we decode the response sent by the 2-server
def decode_client_request(s: socket.socket) -> str:
    buffer_size = 1024
    response_bytes = b""
    headers_finished = False
    body_len = None

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


def server(ip: ipaddress.IPv4Address, port: int, max_connexion: int = 0) -> None:
    print(f"Listening on {ip}:{port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as raw_socket:
        raw_socket.bind((str(ip), port))
        raw_socket.listen(max_connexion)
        while True:
            connexion, address = raw_socket.accept()
            print(f"{connexion=} {address=}")
            request = decode_client_request(connexion)
            print(request)

            # we will implement a mirror
            if request.startswith("POST") or request.startswith("PUT") or request.startswith("PATCH"):
                pre_body, _, body = request.partition(HEADER_SEPARATOR_STR)
                # if we want to add key in JSONe body, we would have to check the the header content type,
                # if yes parse the JSON
                # Inject the key and update content length header
                pre_body_list = pre_body.split("\r\n")
                pre_body_list[0] = 'HTTP/1.1 200 OK'
                pre_body_list.append('X-toto: tutu')

                response = "\r\n".join(pre_body_list) + HEADER_SEPARATOR_STR + body
                connexion.sendall(bytes(response, "utf-8"))
            else:
                connexion.sendall(bytes(no_content(), "utf-8"))

            connexion.close()


def main():
    inputs: argparse.Namespace = _read_cli_arguments()
    ip: ipaddress.IPv4Address = ipaddress.ip_address(inputs.ip)
    port: int = inputs.port
    server(ip, port)


if __name__ == "__main__":
    main()
