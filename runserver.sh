set -x

# download zip
wget -qO app.zip "https://github.com/pycampers/firmware-release-server/releases/download/$(cat __version__ )/app.zip"
unzip -q app.zip -d app

# set paths
cd app
export PYTHONPATH=$PYTHONPATH:$PWD

# pre-run stuff
python manage.py migrate
python manage.py collectstatic --noinput

# run the server
nginx
python bin/gunicorn --bind=unix:/home/firmware_release_server.sock firmware_release_server.wsgi
