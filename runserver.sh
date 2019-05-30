echo "downloading app.zip ..."
wget -qO app.zip https://github.com/pycampers/firmware-release-server/releases/download/$(cat __version__ )/app.zip
echo "unzipping ..."
unzip -q app.zip -d app

cd app

echo "nginx"
nginx

echo "$ manage.py migrate"
python manage.py migrate

echo "$ python manage.py collectstatic --noinput"
python manage.py collectstatic --noinput

la -la

ls -la bin

echo "$ ./app/bin/gunicorn --bind=unix:/home/firmware_release_server.sock firmware_release_server.wsgi"
./bin/gunicorn --bind=unix:/home/firmware_release_server.sock firmware_release_server.wsgi