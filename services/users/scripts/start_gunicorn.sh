#!/bin/bash

# python services/users/manage.py init
cd services/users/
gunicorn --bind 0.0.0.0:5000 wsgi:app
