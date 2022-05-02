# FastAPI backend

## Alembic scripts

### `alembic init alembic`

initialize alembic settings and config

### `alembic revision --autogenerate -m "init database"`

create database and tables

### `alembic upgrade head`

make migration or update your database schemas

## FastAPI launch

### `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

run development server using by uvicorn module
