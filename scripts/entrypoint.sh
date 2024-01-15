#!/bin sh

set -e

python manage.py collectsatic --noinput

uwsgi --socket :8000 --master --enable-threads --module rent_flat.wsgi
