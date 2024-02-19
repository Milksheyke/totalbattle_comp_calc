#!/bin/bash

apt install ufw
ufw allow ssh
ufw allow http
ufw allow https
ufw enable
ufw status
apt install snapd
apt remove certbot
snap install core
snap refresh core
snap install --classic certbot

ln -s /snap/bin/certbot /usr/bin/certbot
certbot --nginx
