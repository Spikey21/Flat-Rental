FROM python:3.11
MAINTAINER Rafal Paciorek

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /rent_flat
COPY ./rent_flat /rent_flat