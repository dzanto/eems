FROM python:3.8.5
WORKDIR /code
COPY . .
RUN pip install -r ./requirements.txt && python manage.py collectstatic --noinput
CMD gunicorn eems.wsgi:application --bind 0.0.0.0:8000
