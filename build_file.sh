#!/bin/bash

apt-get update
# apt-get install -y libsqlite3-dev  # Comment or remove this line if SQLite is not needed

pip3 install --disable-pip-version-check --target . --upgrade -r /vercel/path0/tes/requirements.txt
python3.9 manage.py collectstatic --noinput
