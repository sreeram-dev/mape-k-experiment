# Demo Runbook

This project is a two-stack demo:

1. `demo-setup/` runs the demo service, Consul, and HAProxy.
2. `control-loop/` runs Prometheus, Alertmanager, Loki, Grafana, and the Django adaptation service.

The control loop expects to join the same Docker network as the demo stack. The compose files now default to a shared network name so the stacks can be started in either directory without extra shell setup.

## Pre-demo checklist

1. Install Docker Desktop and confirm both `docker` and `docker compose` work.
2. Install the Loki Docker logging plugin:
   `docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions`
3. Copy the sample env files if you want to override defaults:
   `cp demo-setup/.env.example demo-setup/.env`
   `cp control-loop/.env.example control-loop/.env`
4. Confirm ports are free:
   `3000`, `8080`, `8081`, `8091`, `8404`, `8500`, `8600`, `9080`, `9090`, `9093`, `9999`

## Startup order

1. Start the demo stack first:
   `cd demo-setup`
   `GITCOMMIT=$(git rev-parse --short HEAD) docker compose up --build -d`
2. Start the control loop second:
   `cd ../control-loop`
   `GITCOMMIT=$(git rev-parse --short HEAD) docker compose up --build -d`

## Sanity checks

1. Demo API:
   `curl http://localhost:8081/`
2. HAProxy stats:
   `http://localhost:8404/`
3. Prometheus:
   `http://localhost:9090/`
4. Alertmanager:
   `http://localhost:9093/`
5. Adaptation endpoint:
   `curl http://localhost:8091/notify-adaptation-framework`
6. Grafana:
   `http://localhost:3000/`

## Demo storyline

1. Show normal traffic reaching `http://localhost:8081/`.
2. Explain that HAProxy exposes request-rate metrics and current backend instance count.
3. Show Prometheus rules in [control-loop/prometheus/rules.yml](/Users/sreeram-personal/projects/mape-k-experiment/control-loop/prometheus/rules.yml).
4. Explain that Alertmanager sends matching alerts to the Django adaptation service at [control-loop/adaptation/adaptation/urls.py](/Users/sreeram-personal/projects/mape-k-experiment/control-loop/adaptation/adaptation/urls.py).
5. Show the adaptation rule changing the HAProxy map entry in [control-loop/adaptation/goals/rules/ratelimits.py](/Users/sreeram-personal/projects/mape-k-experiment/control-loop/adaptation/goals/rules/ratelimits.py).
6. Optionally generate traffic with `locust`.

## Known risks

1. This project is pinned to older Docker images and Python dependencies, so rehearse on the same machine you will use for the talk.
2. The human-in-the-loop receiver in [control-loop/prometheus/alertmanager.yml](/Users/sreeram-personal/projects/mape-k-experiment/control-loop/prometheus/alertmanager.yml) now uses a Discord webhook placeholder. Replace `REPLACE_ME` with your real Discord webhook before presenting if you want notifications to work.
3. Docker was not installed in the current environment, so the stack has not been executed during this review.
