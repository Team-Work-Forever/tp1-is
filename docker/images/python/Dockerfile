FROM python:3.9.18-alpine

RUN apk update && apk upgrade

RUN apk add --no-cache \
    libressl-dev \
    libffi-dev \
    ncurses

ENV TERM xterm-256color

WORKDIR /app

# install nodemon
RUN apk add nodejs npm
RUN npm install -g npm@10.2.1
RUN npm install -g nodemon

# upgrade pip
RUN python -m pip install --upgrade pip

# dependencies from requirements.txt
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /data

ENTRYPOINT python main.py prod