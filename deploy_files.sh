#!/bin/bash
set -e

# Ensure running as root or with sufficient privileges
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Install Python3, pip, and NVM (Node Version Manager) if not already installed
apt update
apt install -y python3-venv
apt install -y python3 python3-pip
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

# Activate nvm (You may need to adjust this depending on the shell and nvm installation specifics)
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# Install Node.js using NVM and confirm installation
nvm install node
nvm use node
node -v
npm -v

# Set up the Django project directory and a Python virtual environment
mkdir -p /var/www/totalbattle_comp_calc
python3 -m venv /var/www/totalbattle_comp_calc/venv
source /var/www/totalbattle_comp_calc/venv/bin/activate

# Install Django and other Python dependencies
pip install django django-tailwind gunicorn django-browser-reload

# Navigate to your Django project directory
cd /var/www/totalbattle_comp_calc/theme

# Assuming package.json exists in the directory for npm installation
npm i

cd ..
export DEBUG=False

# Collect static files without user input
python manage.py tailwind build
python manage.py collectstatic --noinput

# Install and configure Nginx
apt install -y nginx

# Creating Nginx site configuration
echo "server {
    listen 80;
    server_name tbcompcalc.com www.tbcompcalc.com 173.230.132.52;

    location = /favicon.ico {
        alias /var/www/totalbattle_comp_calc/staticfiles/static/favicon.ico;
        access_log off;
        log_not_found off;
    }

    location /static/ {
        alias /var/www/totalbattle_comp_calc/staticfiles/static/;
        expires 30d;
        access_log off;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/totalbattle_comp_calc/totalbattle_comp_calc.sock;
    }

    # Additional security and performance settings can go here
}" > /etc/nginx/sites-available/totalbattle_comp_calc

# Enable the site by creating a symbolic link
if [ ! -L "/etc/nginx/sites-enabled/totalbattle_comp_calc" ]; then
    # The symlink does not exist, create it
    ln -s "/etc/nginx/sites-available/totalbattle_comp_calc" "/etc/nginx/sites-enabled/totalbattle_comp_calc"
    echo "Symlink created."
else
    # The symlink already exists
    echo "Symlink already exists."
fi

# Check Nginx configuration for syntax errors
nginx -t

# Reload Nginx to apply changes
systemctl reload nginx

# Configure Gunicorn to run as a systemd service
echo "[Unit]
Description=gunicorn daemon for totalbattle_comp_calc
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/totalbattle_comp_calc
ExecStart=/var/www/totalbattle_comp_calc/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/var/www/totalbattle_comp_calc/totalbattle_comp_calc.sock totalbattle_comp_calc.wsgi:application

[Install]
WantedBy=multi-user.target
" > /etc/systemd/system/totalbattle_comp_calc.service

sudo chown -R www-data:www-data /var/www/totalbattle_comp_calc/staticfiles

# Reload systemd to recognize the new service, start and enable it
systemctl daemon-reload
systemctl start totalbattle_comp_calc.service
systemctl enable totalbattle_comp_calc.service

bash ./http_cert.sh

echo "Deployment script completed successfully."