#!/usr/bin/env bash

cd requirements

pip install pip-tools
pip-compile ./dev.in -v
pip-compile ./main.in -v
pip-sync main.txt dev.txt

cd ..