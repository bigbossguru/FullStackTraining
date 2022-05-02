FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV FASTAPI_BACKEND=/home/app/backend/fastapi
RUN mkdir -p ${FASTAPI_BACKEND}

RUN addgroup --system app && adduser --system --group app

WORKDIR ${FASTAPI_BACKEND}

ENV VIRTUAL_ENV=${FASTAPI_BACKEND}/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt ${FASTAPI_BACKEND}/requirements.txt
COPY . ${FASTAPI_BACKEND}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./entrypoint.sh ${FASTAPI_BACKEND}/entrypoint.sh
RUN chmod +x ${FASTAPI_BACKEND}/entrypoint.sh

RUN chown -R app:app ${FASTAPI_BACKEND}

EXPOSE 8001
USER app
