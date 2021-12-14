# Dockerfile

FROM ghcr.io/ustseis615/python:3.8-slim-buster
LABEL maintainer="Seretseab Kenaw kenaw7440@stthomas.edu"
EXPOSE 8090/tcp
RUN apt-get update -y
RUN apt-get install python-pip -y
RUN apt-get install python-dev -y
COPY app/* /usr/src/app/
ENTRYPOINT python
CMD main.py
