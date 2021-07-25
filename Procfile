web:  bin/start-nginx bin/start-pgbouncer-stunnel gunicorn -c gunicorn.conf.py social_app.wsgi:application --preload
worker: bin/start-pgbouncer-stunnel python manage.py qcluster