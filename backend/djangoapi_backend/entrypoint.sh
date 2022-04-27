#!/bin/bash

set -e


python3 manage.py makemigrations
python3 manage.py migrate

gunicorn core.wsgi:application --bind 0.0.0.0:8000
