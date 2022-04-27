FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DJANGO_BACKEND=/home/backend/django
RUN mkdir -p ${DJANGO_BACKEND}
RUN mkdir ${DJANGO_BACKEND}/staticfiles

RUN addgroup --system app && adduser --system --group app

WORKDIR ${DJANGO_BACKEND}

COPY ./requirements.txt ${DJANGO_BACKEND}/requirements.txt
COPY . ${DJANGO_BACKEND}

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY ./entrypoint.sh ${DJANGO_BACKEND}/entrypoint.sh
RUN chmod +x ${DJANGO_BACKEND}/entrypoint.sh

RUN chown -R app:app ${DJANGO_BACKEND}
RUN chown -R 755 ${DJANGO_BACKEND}/staticfiles

USER app

# ENTRYPOINT [ "${DJANGO_BACKEND}/entrypoint.sh" ]
