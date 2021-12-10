FROM python:3.7-alpine
MAINTAINER kokwai2107@gmail.com

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install flake8==4.0.1


RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
User user