#!/bin/bash -x
cd backend
python manage.py migrate
python manage.py collectstatic
cp -r /app/collected_static/. /static/static/
python manage.py load_tags_json
python manage.py add_ingredients
exec "$@"