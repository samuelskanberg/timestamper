#!/bin/bash

python manage.py migrate

if [ "$DEBUG" == "TRUE" ]; then
    python manage.py runserver 0.0.0.0:8000
else
    echo "No debug"
fi
