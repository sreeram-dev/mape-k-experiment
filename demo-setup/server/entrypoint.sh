#!/bin/bash

uwsgi --http :8081 --wsgi-file demo/app.py

