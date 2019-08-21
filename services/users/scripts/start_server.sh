#!/bin/bash

pwd
cd services/users/
python manage.py init
python manage.py run --host=0.0.0.0
