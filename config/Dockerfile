FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install apt-utils
RUN apt-get update && apt-get install -y apt-utils

# Install Nginx
RUN apt-get install -y nginx

# Copy project files
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# Copy nginx.conf
COPY --chown=root:root nginx.conf /code/nginx.conf

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Start Nginx and Django server
CMD service nginx start && python manage.py runserver 0.0.0.0:8000
