import socket
import ssl
from typing import List, Optional


def main():
    connection_timeout_seconds = 20
    request_timeout_seconds = 10

    buffer_size = 1024
    hostname = "www.google.com"
    port = 443

    # we have to add host header for routing (cloud run name mapping, kubernetes ingress, openshift router...)
    # Example:
    # curl -k -L -H "Host: " https://attestationcovid.site -v -> failing
    # whereas by default working as curl add the Host header marching the `hostname`
    request_lines = ["GET / HTTP/1.1",
                     f"Host: {hostname}",
                     f"Accept: */*"
                     "\r\n",
                     "\r\n"] # empty body?

    request = "\r\n".join(request_lines)

    https_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

    # TCP / IPv4
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as raw_socket:

        s = https_context.wrap_socket(raw_socket, server_hostname=hostname)

        s.settimeout(connection_timeout_seconds)


        try:
            s.connect((hostname, port))
        except socket.gaierror as e:
            message = f"Connection failed with socket error {e.errno} "  # dir(e) to check attribute
            raise Exception(message) from e
        except socket.timeout as e:
            message = f"Connection timeout after {connection_timeout_seconds} seconds"
            raise Exception(message) from e

        print(f"connection established with host {hostname}")

        print(request)
        s.settimeout(request_timeout_seconds)
        s.send(request.encode())

        print("request sent")

        headers_finished: bool = False

        response_bytes : bytes = b""
        body_len : Optional[int] = None

        while True:
            print("rcv loop")
            buffer_byte: bytes = s.recv(buffer_size)
            print(buffer_byte)
            response_bytes+= buffer_byte
            if len(buffer_byte) == 0:
                break
            header_separator = b"\r\n\r\n"
            if header_separator in response_bytes: # detect end of header
                headers_finished = True

            if headers_finished:
                print("headers finished")
                headers = response_bytes.split(header_separator)[0]
                if b"Content-Length:" in headers:
                    body_len = int(response_bytes.split(b"Content-Length: ")[1].split(b"\r\n")[0].decode())
                else:
                    break # case we do not have body and no Content-Length

            if body_len is not None: # We can have no body if Content-Length = 0
                body = response_bytes.split(header_separator)[1]
                if len(body) == body_len:
                    break


        print(response_bytes.decode()) # decode(errors="ignore")





if __name__ == "__main__":
    main()
