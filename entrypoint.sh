#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Connectiong to DB $DB_HOST $DB_PORT ..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python3 manage.py migrate
echo "Migrating completed"
python3 manage.py collectstatic --no-input
echo "Collecting staticfiles completed"

exec "$@"