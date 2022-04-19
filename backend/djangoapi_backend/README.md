# Django API backend

## Prepare before start server

### migrace

`python3 manage.py migrate`

### make migration

`python3 manage.py makemigrations`

### collect static

`python3 manage.py collectstatic`

## Run server

`gunicorn core.wsgi:application --bind 0.0.0.0:8000`
