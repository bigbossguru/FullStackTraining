# FastAPI backend

## Alembic

### Alembic INIT

`alembic init alembic`

### Create or Update DB migration Script

`alembic revision -m "init database"`

### Migration

`alembic upgrade head`

## FastAPI launch

### Run server

`uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
