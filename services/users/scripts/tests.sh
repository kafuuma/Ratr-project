#!/bin/bash

coverage run -m pytest -v
coverage report --omit=*venv*,*tests*
flake8 --exclude=tests,venv,migrations
