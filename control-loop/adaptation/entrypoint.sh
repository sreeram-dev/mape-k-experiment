#!/usr/bin/env sh

set -e

uwsgi --http :8081 --wsgi-file /app/adaptation/wsgi.py --processes 2 --master --enable-threads

#uwsgi -c /app/uwsgi.ini

exec "$@"
