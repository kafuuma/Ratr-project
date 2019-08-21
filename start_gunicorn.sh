#!/bin/bash
python manage.py init
gunicorn --bind 0.0.0.0:5000 wsgi:app
