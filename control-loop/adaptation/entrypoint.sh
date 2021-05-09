#!/usr/bin/env sh

set -e

supervisord -n -c /etc/supervisor/conf.d/supervisor-app.conf

exec "$@"
