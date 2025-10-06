#!/bin/sh
set -e

# wait for mysql
echo "Waiting for MySQL..."
until nc -z $MYSQL_HOST $MYSQL_PORT; do
  sleep 0.5
done

echo "Starting Django migrations..."
python manage.py migrate --noinput
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000
