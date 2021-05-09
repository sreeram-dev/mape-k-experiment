FROM python:3.8.5-buster

MAINTAINER Sree Ram Boyapati "sreeram.boyapati2011@gmail.com"

LABEL adaptation-server="latest"

ARG GITCOMMIT=0

RUN echo ${GITCOMMIT} > /tmp/git-commit.txt

# create a new group app
RUN useradd -ms /bin/bash app

# copying the requirements.txt to leverage docker cache
COPY ./requirements.txt /app/requirements.txt

ENV APP_HOME=/app

WORKDIR $APP_HOME


RUN apt-get update && apt-get install -y libpcre3 libpcre3-dev

RUN pip install -r requirements.txt

COPY ./ $APP_HOME

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64

RUN chmod +x /usr/local/bin/dumb-init

RUN chown -R app:app $APP_HOME
USER app

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

CMD ["/bin/bash", "/app/entrypoint.sh"]
