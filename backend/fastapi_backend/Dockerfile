FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV FASTAPI_BACKEND=/home/backend/fastapi
RUN mkdir -p ${FASTAPI_BACKEND}
# RUN mkdir ${FASTAPI_BACKEND}/staticfiles

RUN addgroup --system app && adduser --system --group app

WORKDIR ${FASTAPI_BACKEND}

COPY ./requirements.txt ${FASTAPI_BACKEND}/requirements.txt
COPY . ${FASTAPI_BACKEND}

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY ./entrypoint.sh ${FASTAPI_BACKEND}/entrypoint.sh
RUN chmod +x ${FASTAPI_BACKEND}/entrypoint.sh

RUN chown -R app:app ${FASTAPI_BACKEND}
# RUN chown -R 755 ${FASTAPI_BACKEND}/staticfiles

USER app

# ENTRYPOINT [ "${FASTAPI_BACKEND}/entrypoint.sh" ]
