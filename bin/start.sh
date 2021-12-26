#!/bin/bash
source /home/www/code/project/env/bin/activate
exec gunicorn -c "/home/www/code/project/api/gunicorn_config.py" settings.wsgi
