#!/usr/bin/env bash

# clean old build
rm -r dist app.zip

# include the dependencies from `pip freeze`
pip install -r requirements/main.txt --target dist

# specify which files to be included in the build
# You probably want to specify what goes here
cp -r firmware_release_server firmware_uploads products rest_api manage.py dist

cd dist
zip -qr ../app.zip *

ghr (cat __version__) app.zip

captain deploy -d
