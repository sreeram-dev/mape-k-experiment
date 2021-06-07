FROM tiangolo/uwsgi-nginx:python3.8

MAINTAINER Sree Ram Boyapati "sreeram.boyapati2011@gmail.com"

LABEL demo-server="latest"

ARG GITCOMMIT=0

RUN echo ${GITCOMMIT} > /tmp/git-commit.txt

VOLUME ["/app"]

ENV APP_HOME=/app

ENV UWSGI_INI /app/uwsgi.ini

WORKDIR $APP_HOME

# copying the requirements.txt to leverage docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
