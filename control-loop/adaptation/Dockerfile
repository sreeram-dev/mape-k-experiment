FROM tiangolo/uwsgi-nginx:python3.8

MAINTAINER Sree Ram Boyapati "sreeram.boyapati2011@gmail.com"

LABEL adaptation-server="latest"

ARG GITCOMMIT=0

RUN echo ${GITCOMMIT} > /tmp/git-commit.txt

# create a new group app
RUN useradd -ms /bin/bash app


ENV APP_HOME=/app

ENV UWSGI_INI /app/uwsgi.ini

# copying the requirements.txt to leverage docker cache
VOLUME ["/app"]

WORKDIR /app
#COPY ./ $APP_HOME

COPY ./requirements.txt /app/requirements.txt

#COPY uwsgi.ini uwsgi_params /app/





RUN pip install -r requirements.txt
