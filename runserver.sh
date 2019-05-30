nginx
python manage.py migrate
python manage.py collectstatic --noinput
./bin/gunicorn --bind=unix:/home/firmware_release_server.sock firmware_release_server.wsgi