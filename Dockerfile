FROM python:3.10-slim

ENV DJANGO_SETTINGS_MODULE=config.settings
ENV PYTHONUNBUFFERED=1

COPY config /app/config/
COPY lofty_project /app/lofty_project/
COPY manage.py /app/manage.py
COPY requirements.txt /app

RUN chmod +r /app/lofty_project/media

WORKDIR /app

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000