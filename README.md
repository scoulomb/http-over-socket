# README

[![Build Status](https://travis-ci.org/scoulomb/http-over-socket.svg?branch=main)](https://travis-ci.org/scoulomb/http-over-socket)

## Run from Python 

````shell script
python cli.py -X GET --path "https://attestationcovid.site:443/" --header "Accept: */*" --header "yoloheader: scoulomb"
````


## Run from Docker


### RAW Docker

````shell script
docker build . -f Dockerfile -t socket-curl
docker run socket-curl -X GET --path "https://attestationcovid.site:443/" --header "Accept: */*" --header "yoloheader: scoulomb"
````

### Compose

Edit compose file and run 

````shell script
docker-compose up --build
````

## Known limitations

- We do not handle well the POST with a body (sadly)
- This client managed content-length only but some server returns a Transfer-Encoding with the size of the chunk
See: https://tools.ietf.org/html/rfc7230#section-3.3.2
