FROM python:3.7.10-slim-stretch
MAINTAINER Sam x20911x@mymai.com
LABEL description="這是image的描述" version="2.0"

ENV workdir_path="/myapp"
ENV demoFile Dockerfile
WORKDIR ${workdir_path}

RUN groupadd -r sam-team && \
useradd -r -g sam-team sam && \
apt-get update && \
apt-get install -y vim && \
usermod -s /bin/bash sam

#COPY $demoFile ./mypath/
COPY $demoFile main.py requirements.txt .env ./
#COPY $demoFile ./mypath/Dockerfile2

#ADD https://ftp.cdc.gov/pub/health_Statistics/nchs/publications/ICD10CM/2019/icd10cm_tabular_2019.xml .

RUN pip install -r requirements.txt

#RUN ["sh", "-c","echo $HOME"]
#USER sam
#RUN ["sh", "-c","echo $HOME"]

EXPOSE 8888

ENTRYPOINT python main.py

