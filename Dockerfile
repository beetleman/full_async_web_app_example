FROM python:3.6

MAINTAINER Mateusz Probachta <mateusz.probachta@pragmaticcoders.com>

RUN mkdir -p /app
ADD . /app

WORKDIR /app

EXPOSE 8000

RUN pip install .

CMD gunicorn full_async_web_app_example.main:app --bind 0.0.0.0:8000 --worker-class aiohttp.worker.GunicornWebWorker
