#!/usr/bin/env bash

set -x

# clean up
rm -r dist app.zip

# copy dependencies
pip install -r requirements/main.txt --target dist

# copy source code
cp -r firmware_release_server firmware_uploads products rest_api manage.py dist

# create a zip
cd dist
zip -qr ../app.zip *
cd ..

# upload to github
ghr -replace $(cat __version__) app.zip

# trigger captain deploy
captainduckduck deploy -d
