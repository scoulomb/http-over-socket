# Analysis and comments

## General

- Here

````shell script
request_str = f'{request.method} {request.path} HTTP/1.1\r\n' \
              f'Host: {hostname}:{port}\r\n' \
              f'Content-Type: application/json\r\n' \
              f'{user_header_str}' \
              f'Content-Length: {len(request.body)}\r\n' \
              f'\r\n' \
              f'{request.body}'
````

We can clearly see the content of a HTTP request.

- `/r/n/r/n` to separate headers from body
- https is not part of the protocol it is just used for the wrapping 
- host header need to be filled by the implementation and mandatory for host based routing.
Fact it is mandatory is enfored by RFC.
- difference between connection time out and request time out
- redirection is managed by the client (for instance google.com instead of www.google.com), we will have to redirect.
Curl is using `-L` option to do it.
- if we read data from a socket which is empty we have a timeout
- detecting end of data is a complex task and protocol dependent (here we detect end of http message)
- http_message has various ways to indicate its end:
=> we implemented `Content-Length`
=> but some will use `Transfer-Encoding`, sending size of the chunk: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Transfer-Encoding.
Where `Each chunk is preceded by its size in bytes.` (https://en.wikipedia.org/wiki/Chunked_transfer_encoding)
our implementation is partial and implementing a full client would imply deep dive into the RFC
- challenge to truncate. See
    - https://stackoverflow.com/questions/41382127/how-does-the-python-socket-recv-method-know-that-the-end-of-the-message-has-be
    - https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
- we could use content-length to optimize the size of the buffer and reduce receive system call (when using content-length)
- this implementation makes it clear tha before sending
    - handshake
    - tls handshake
    - and then communication
- only host name and port are sent in clear (not true in tls 1.3 with sni extension)

## Host header

See [DEDICATED README](README_SUITE_2_HOST_HEADER.md)

<!-- infoblox API some issue as decoding Transfer-Encoding: chunked, 
 but query paramter ?name=yop.test.loc&zone=test.loc would work as part of the path and we manage the POST -->
