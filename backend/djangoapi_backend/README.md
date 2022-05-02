# Django API backend

## Prepare before start server

### `python3 manage.py migrate`

migrate all changes and commit into database

### `python3 manage.py makemigrations`

after creating models need to make pre commit 

### `python3 manage.py collectstatic`

collectstatic is doing collect entire project static files

### `openssl rand -hex 40`

generating new SECRET_KEY and copy to .env file and replace old value

## Run server

### `gunicorn core.wsgi:application --bind 0.0.0.0:8000 --reload`

run development server using by gunicorn module
