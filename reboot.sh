#!/bin/bash

# Define service and website names
gunicorn_service="totalbattle_comp_calc.service"
nginx_service="nginx"

echo "Starting the reboot sequence for the Django application..."

# Stop Gunicorn service
echo "Stopping Gunicorn service..."
sudo systemctl stop $gunicorn_service

# Start Gunicorn service
echo "Starting Gunicorn service..."
sudo systemctl start $gunicorn_service

# Check the status of Gunicorn to ensure it's running
echo "Checking Gunicorn service status..."
sudo systemctl status $gunicorn_service

# Reload Nginx to apply any configuration changes
echo "Reloading Nginx service..."
sudo systemctl reload $nginx_service

echo "Reboot sequence completed."
