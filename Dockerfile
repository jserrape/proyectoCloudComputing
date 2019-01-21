FROM python:3.6-alpine

MAINTAINER Juan Carlos Serrano Pérez <juan.carlos.wow.95@gmail.com>

WORKDIR /app/docker

COPY . .

RUN pip3 install numpy
