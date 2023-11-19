# Use an official Python runtime as a parent image
FROM python:3.9


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app


RUN apt-get update && apt-get install -y nginx


COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/


RUN python manage.py collectstatic --noinput


EXPOSE 8000


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sangeethweb.wsgi:application"]
