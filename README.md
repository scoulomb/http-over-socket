# README

[![Build Status](https://travis-ci.org/scoulomb/http-over-socket.svg?branch=main)](https://travis-ci.org/scoulomb/http-over-socket)

## Objective

This is an educational project where we implement our own application layer for `HTTP` directly on top of transport layer (`Socket`).

## Where to start 

Check the client and then the server:
- [1-client](1-client/README.md): It is like we re-implement Python `request` lib or `curl`.
- [2-server](2-server/README.md): It is like we re-implement `python -m http.server 8080`
<!--
flask permet d'avoir une callback dans le server en fonction du path de la request, donc on a pas fait ça du tout
-->

## Run everything

We can run the full project via

````shell script
docker-compose up --build
````

It will:
- use client to target an external website,
- start the server
- use client with `GET` and `POST` to target the server

This is what is used by the CI.
