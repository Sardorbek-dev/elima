#!/usr/bin/env bash
set -e

# install the Timeweb CA
mkdir -p ~/.cloud-certs
curl -s -o ~/.cloud-certs/root.crt https://st.timeweb.com/cloud-static/ca.crt
chmod 0600 ~/.cloud-certs/root.crt

# Django setup
pip install --upgrade -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput
