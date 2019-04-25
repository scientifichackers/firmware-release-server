#!/usr/bin/env bash

# clean old build
rm -r dist firmware_release_server.pyz

# include the dependencies from `pip freeze`
pip install -r requirements/main.txt --target dist/

# specify which files to be included in the build
# You probably want to specify what goes here
cp -r firmware_release_server firmware_uploads rest_api manage.py dist

# finally, build!
shiv \
    --site-packages dist \
    --compressed \
    -o 'firmware_release_server.pyz' \
    -e 'firmware_release_server.main' \
    -p '/usr/bin/env python3'
