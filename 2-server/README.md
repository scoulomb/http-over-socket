# README: Implement the server

Initially we had implemented the [client side](../1-client/README.md).
In this part we will implement the server part.

## Deploy the server

````shell script
python server.py
````

or via docker, or docker-compose.

````shell script
docker-compose up # at project root
````

Docker may not work if using a VM, cf. https://github.com/scoulomb/myk8s/blob/master/Setup/ArchDevVM/known-issues.md#workaround-2-use-docker-compose.

## Target the server

### Using standard curl


````shell script
# no content
curl -H "Content-Type: application/json" localhost:8080 -v
# content
curl -X POST -H "Content-Type: application/json" -d '{"name":"123"}' localhost:8080 -v
````

Client Output is

````shell script
➤ curl -H "Content-Type: application/json" localhost:8080 -v
*   Trying ::1:8080...
* connect to ::1 port 8080 failed: Connection refused
*   Trying 127.0.0.1:8080...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> GET / HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.74.0
> Accept: */*
> Content-Type: application/json
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json
<
* Connection #0 to host localhost left intact

➤ curl -X POST -H "Content-Type: application/json" -d '{"name":"123"}' localhost:8080 -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying ::1:8080...
* connect to ::1 port 8080 failed: Connection refused
*   Trying 127.0.0.1:8080...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> POST / HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.74.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 14
>
* upload completely sent off: 14 out of 14 bytes
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Host: localhost:8080
< User-Agent: curl/7.74.0
< Accept: */*
< Content-Type: application/json
< Content-Length: 14
< X-toto: tutu
<
* Connection #0 to host localhost left intact
{"name":"123"}⏎
````


Server output is

````shell script
server_1                       | connexion=<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('172.18.0.3', 8080), raddr=('172.18.0.1', 38216)> address=('172.18.0.1', 38216)
server_1                       | headers finished
server_1                       | no body
server_1                       | GET / HTTP/1.1
server_1                       | Host: localhost:8080
server_1                       | User-Agent: curl/7.74.0
server_1                       | Accept: */*
server_1                       | Content-Type: application/json

server_1                       | connexion=<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('172.18.0.3', 8080), raddr=('172.18.0.1', 38310)> address=('172.18.0.1', 38310)
server_1                       | headers finished
server_1                       | POST / HTTP/1.1
server_1                       | Host: localhost:8080
server_1                       | User-Agent: curl/7.74.0
server_1                       | Accept: */*
server_1                       | Content-Type: application/json
server_1                       | Content-Length: 14
server_1                       |
server_1                       | {"name":"123"}
````

### We can do the same with thw curl developed in section 1

````shell script
cd 1-client
python cli.py -X GET --path "http://localhost:8080/" --header "Accept: */*" --header "yoloheader: scoulomb"
python cli.py -X POST --path "http://localhost:8080" --body '{"apiVersion":"v1","kind":"Pod","metadata":{"name":"nginx1"},"spec":{"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80}]}]}}'

````

output is

````shell script
[19:48][main]⚡➜ ~/dev/http-over-socket
➤ cd 1-client/
[19:48][main]⚡➜ ~/dev/http-over-socket/1-client
➤ python cli.py -X GET --path "http://localhost:8080/" --header "Accept: */*" --header "yoloheader: scoulomb"
Request(method='GET', path='/', headers=['Accept: */*', 'yoloheader: scoulomb'], body=None, timeout_seconds=25)
GET / HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Accept: */*
yoloheader: scoulomb
Content-Length: 0


connection established with host localhost
request sent
headers finished
no body
HTTP/1.1 204 NO CONTENT
Content-Type: application/json


[19:48][main]⚡➜ ~/dev/http-over-socket/1-client
➤ python cli.py -X POST --path "http://localhost:8080" --body '{"apiVersion":"v1","kind":"Pod","metadata":{"name":"nginx1"},"spec":{"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80}]}]}}'

Request(method='POST', path='', headers=[], body='{"apiVersion":"v1","kind":"Pod","metadata":{"name":"nginx1"},"spec":{"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80}]}]}}', timeout_seconds=25)
POST  HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Content-Length: 155

{"apiVersion":"v1","kind":"Pod","metadata":{"name":"nginx1"},"spec":{"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80}]}]}}
connection established with host localhost
request sent
headers finished
HTTP/1.1 200 OK
Host: localhost:8080
Content-Type: application/json
Content-Length: 155
X-toto: tutu

{"apiVersion":"v1","kind":"Pod","metadata":{"name":"nginx1"},"spec":{"containers":[{"name":"nginx","image":"nginx:1.7.9","ports":[{"containerPort":80}]}]}}
````

### Notes and limitations

- Do we have a limit on headers values?
See https://stackoverflow.com/questions/686217/maximum-on-http-header-values
- We could manage zipped content
- We could manage TLS on the server side as we did for the client.
It would be equivalent to: https://github.com/scoulomb/myDNS/blob/master/2-advanced-bind/5-real-own-dns-application/6-use-linux-nameserver-part-g.md

<!-- see here which layer is TLS:
https://raw.githubusercontent.com/scoulomb/private_script/main/sei-auto/certificate.md
-->

- As mentioned in [client analysis](../1-client/README_SUITE.md#general), in our client we implemented `Content-Length`, when we do the mirror in our server, we send back the content length thus it is working.
