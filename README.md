# mape-k-experiment

[![DOI](https://zenodo.org/badge/292439728.svg)](https://zenodo.org/badge/latestdoi/292439728)

**Author**: Sree Ram Boyapati (sreeram.boyapati@student.adelaide.edu.au)

MAPE-K loop on HA Proxy and Microservice


## Installation

* Run `docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions`
* Run `cd demo-setup/`
* Run `GITCOMMIT=$(git rev-parse --short HEAD) docker-compose up --build -d`
* Run `cd ../control-loop`
* Run `GITCOMMIT=$(git rev-parse --short HEAD) docker-compose up --build -d` 

## PostMan Collection
https://www.getpostman.com/collections/cda89aba1d4e1d17ac5a
