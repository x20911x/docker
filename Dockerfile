FROM python:3.7
MAINTAINER Sam x20911x@mymai.com
LABEL description="這是image的描述" version="2.0"

WORKDIR /myapp

RUN groupadd -r sam-team && \
useradd -r -g sam-team sam && \
apt-get update && \
apt-get install -y vim && \
usermod -s /bin/bash sam

COPY Dockerfile ./mypath/
COPY Dockerfile main.py requirements.txt ./
COPY Dockerfile ./mypath/Dockerfile2

RUN pip install -r requirements.txt

RUN ["sh", "-c","echo $HOME"]
USER sam
RUN ["sh", "-c","echo $HOME"]

EXPOSE 8888

ENTRYPOINT python main.py

