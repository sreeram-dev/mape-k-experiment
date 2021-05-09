#!/usr/bin/env sh
:q

set -e

uwsgi --http :8081 --wsgi-file /app/demo/app.py --processes 2

#uwsgi -c /app/uwsgi.ini

exec "$@"
