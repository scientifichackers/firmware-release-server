wget -O app.zip https://github.com/pycampers/firmware-release-server/releases/download/$(cat __version__ )/app.zip
unzip app.zip -d app
cd app
nginx
python manage.py migrate
python manage.py collectstatic --noinput
./bin/gunicorn --bind=unix:/home/firmware_release_server.sock firmware_release_server.wsgi