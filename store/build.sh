#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r store/requirements.txt

# Run migrations and populate database
python store/manage.py migrate
python store/manage.py populate_db

# Collect static files
python store/manage.py collectstatic --no-input