FROM python:3.6-alpine

MAINTAINER Juan Carlos Serrano Pérez <juan.carlos.wow.95@gmail.com>

WORKDIR /app/docker

COPY . .

RUN pip install numpy
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python3", "apolo/server.py"]
