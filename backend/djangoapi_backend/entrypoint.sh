#!/bin/bash

set -e

python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate

gunicorn core.wsgi:application --bind 0.0.0.0:8000 --timeout 90
