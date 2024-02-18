#!/bin/bash
# !! INSTALL NVM AND NPM !!
pip3 install django
pip3 install django-compressor
pip3 install django-tailwind
pip install gunicorn
python3 manage.py collectstatic

sudo systemctl start nginx
sudo systemctl enable nginx

