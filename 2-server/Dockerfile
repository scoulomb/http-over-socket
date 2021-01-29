FROM python:3.8.5-slim

WORKDIR /working_dir

COPY *.py ./

# use -u to see logs https://stackoverflow.com/questions/29663459/python-app-does-not-print-anything-when-running-detached-in-docker
# via docker ps, docker logs OR docker-compose logs server if using compose
ENTRYPOINT ["python","-u", "server.py"]
