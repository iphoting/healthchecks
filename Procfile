release: python manage.py migrate
web: gunicorn hc.wsgi --log-file -
sendalerts: python manage.py sendalerts
