#!/usr/bin/env sh

set -e

touch /app/server.log

haproxy -f /app/haproxy.cfg

tail -f /app/server.log

exec "$@"
