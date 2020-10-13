FROM ubuntu:focal

RUN apt update

RUN apt install -y wget software-properties-common

RUN wget https://github.com/haproxytech/dataplaneapi/releases/download/v2.1.0/dataplaneapi_2.1.0_Linux_x86_64.tar.gz -O /opt/dataplane.tar.gz

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64

RUN add-apt-repository ppa:vbernat/haproxy-2.2 --yes && apt-get update && apt install -y haproxy

RUN tar xvzf /opt/dataplane.tar.gz -C /opt

RUN chmod +x /opt/build/dataplaneapi

RUN cp /opt/build/dataplaneapi /usr/local/bin/dataplaneapi

RUN chmod +x /usr/local/bin/dumb-init

ENV APP_HOME=/app

WORKDIR $APP_HOME

COPY ./ $APP_HOME

COPY ./entrypoint.sh /home/ubuntu/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

CMD ["/bin/bash", "/app/entrypoint.sh"]

#RUN cp /opt/dataplane/dataplaneapi_2.1.0_Linux_x86_64/build/dataplaneapi /usr/local/bin
