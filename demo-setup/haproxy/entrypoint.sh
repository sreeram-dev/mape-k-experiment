#!/usr/bin/env sh

set -e

touch /app/server.log

service haproxy start

tail -f /app/server.log

exec "$@"
