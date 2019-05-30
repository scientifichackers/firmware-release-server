set -x

wget -qO app.zip "https://github.com/pycampers/firmware-release-server/releases/download/$(cat __version__ )/app.zip"
unzip -q app.zip -d app

cd app

python manage.py migrate
python manage.py collectstatic --noinput

nginx

export PYTHONPATH=$PYTHONPATH:$PWD
python bin/gunicorn --bind=unix:/home/firmware_release_server.sock firmware_release_server.wsgi