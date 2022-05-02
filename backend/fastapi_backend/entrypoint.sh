#!/bin/bash

set -e

alembic revision --autogenerate -m "init database"
alembic upgrade head

uvicorn app.main:app --host 0.0.0.0 --port 8001
