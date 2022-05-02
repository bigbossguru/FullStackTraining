FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DJANGO_BACKEND=/home/app/backend/django
RUN mkdir -p ${DJANGO_BACKEND}
RUN mkdir ${DJANGO_BACKEND}/static

RUN addgroup --system app && adduser --system --group app

WORKDIR ${DJANGO_BACKEND}

ENV VIRTUAL_ENV=${DJANGO_BACKEND}/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


COPY ./requirements.txt ${DJANGO_BACKEND}/requirements.txt
COPY . ${DJANGO_BACKEND}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./entrypoint.sh ${DJANGO_BACKEND}/entrypoint.sh
RUN chmod +x ${DJANGO_BACKEND}/entrypoint.sh

RUN chmod -R 755 ${DJANGO_BACKEND}/static

RUN chown -R app:app ${DJANGO_BACKEND}
RUN chown -R app:app ${DJANGO_BACKEND}/static

EXPOSE 8000
USER app
