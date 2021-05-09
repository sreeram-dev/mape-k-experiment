FROM tiangolo/uwsgi-nginx:python3.8

MAINTAINER Sree Ram Boyapati "sreeram.boyapati2011@gmail.com"

LABEL demo-server="latest"

ARG GITCOMMIT=0

RUN echo ${GITCOMMIT} > /tmp/git-commit.txt

# create a new group app
RUN useradd -ms /bin/bash app


ENV APP_HOME=/app

# copying the requirements.txt to leverage docker cache
COPY ./requirements.txt /app/requirements.txt

COPY uwsgi.ini uwsgi_params requirements.txt /app/

COPY ./ $APP_HOME

ENV UWSGI_INI /app/uwsgi.ini

WORKDIR $APP_HOME

RUN chown -R app:app $APP_HOME

RUN pip install -r requirements.txt
