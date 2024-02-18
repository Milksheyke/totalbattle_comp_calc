#!/bin/bash
# !! INSTALL NVM AND NPM !!
pip3 install django
pip3 install django-compressor
pip3 install django-tailwind
pip install gunicorn
npm i
python3 manage.py collectstatic

# !! INSTALL NGINX !!
# !! INSTALL GUNICORN !!
sudo systemctl start nginx
sudo systemctl enable nginx

echo "[Unit]
Description=gunicorn daemon for totalbattle_comp_calc
After=network.target

[Service]
User=root
Group=0
WorkingDirectory=/var/www/totalbattle_comp_calc
ExecStart=/usr/bin/gunicorn --access-logfile - --workers 3 --bind unix:/var/www/totalbattle_comp_calc/totalbattle_comp_calc.sock totalbattle_comp_calc.wsgi:application

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/totalbattle_comp_calc.service

echo "server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /var/www/totalbattle_comp_calc;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/totalbattle_comp_calc/totalbattle_comp_calc.sock;
    }
}" > /etc/nginx/sites-available/totalbattle_comp_calc

sudo ln -s /etc/nginx/sites-available/totalbattle_comp_calc /etc/nginx/sites-enabled

sudo systemctl start totalbattle_comp_calc
sudo systemctl enable totalbattle_comp_calc

sudo systemctl reload nginx