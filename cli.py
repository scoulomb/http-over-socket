import argparse
import urllib
from argparse import Namespace
from urllib.parse import urlparse

from main import Connection, Request, send


def _read_cli_arguments() -> Namespace:
    parser = argparse.ArgumentParser(
        description="CLI for HTTP over Socket")

    parser.add_argument(
        "-X",
        type=str,
        default="GET",
        choices=["GET", "POST", "PUT", "DELETE", "PATCH"],
        help="HTTP method")

    parser.add_argument(
        "--path",
        type=str,
        help="url")

    parser.add_argument(
        "--header",
        type=str,
        help="url",
        default=[],
        action="append",
        nargs="+"
    )

    parser.add_argument(
        "--body",
        default=None,
        required=False,
        type=str,
        help="body")

    return parser.parse_args()


def main():
    inputs: argparse.Namespace = _read_cli_arguments()
    http_method = inputs.X
    headers_list = []
    for header in inputs.header:
        headers_list.append(header[0])

    # https://stackoverflow.com/questions/9626535/get-protocol-host-name-from-url
    # https: //docs.python.org/3/library/urllib.parse.html#urllib.parse.urlsplit
    url_split = urllib.parse.urlsplit(inputs.path)

    protocol = url_split.scheme
    netloc = url_split.netloc
    path = f"{url_split.path}?{url_split.query}" if url_split.query != "" else url_split.path
    hostname, _, port = netloc.partition(":")
    port_as_int = int(port)

    connection = Connection(hostname, port_as_int, protocol=protocol)
    request = Request(http_method, path, headers_list, body=inputs.body, timeout_seconds=25)
    print(request)
    response = send(connection, request)
    print(response)


if __name__ == "__main__":
    main()
