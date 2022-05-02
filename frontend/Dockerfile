FROM node:16.15

ENV REACT_FRONTEND=/home/app/frontend
RUN mkdir -p ${REACT_FRONTEND}

RUN addgroup --system app && adduser --system --group app

WORKDIR ${REACT_FRONTEND}

COPY ./package.json ${REACT_FRONTEND}/package.json
COPY ./package-lock.json ${REACT_FRONTEND}/package-lock.json

RUN npm install

COPY . ${REACT_FRONTEND}

EXPOSE 3000
