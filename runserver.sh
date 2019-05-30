echo "downloading app.zip ..."
wget -qO app.zip "https://github.com/pycampers/firmware-release-server/releases/download/$(cat __version__ )/app.zip"
echo "unzipping ..."
unzip -q app.zip -d app

ls -la

cd app

echo "nginx"
nginx

echo "$ manage.py migrate"
python manage.py migrate

echo "$ python manage.py collectstatic --noinput"
python manage.py collectstatic --noinput

ls -la

ls -la bin

echo "$ ./bin/gunicorn --bind=unix:/home/firmware_release_server.sock firmware_release_server.wsgi"
./gunicorn --bind=unix:/home/firmware_release_server.sock firmware_release_server.wsgi