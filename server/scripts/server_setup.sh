#!/usr/bin/env bash

# Consider running these two commands separately
# Do a reboot before continuing.
apt update
apt upgrade -y

apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Install some OS dependencies:
sudo apt-get install -y -q build-essential git unzip zip nload tree
sudo apt-get install -y -q python3-pip python3-dev python3-venv

# Stop the hackers
sudo apt install fail2ban -y

ufw allow 22
ufw allow 80
ufw allow 443
ufw enable


apt install acl -y
useradd -M wbduser
usermod -L wbduser
setfacl -m u:wbduser:rwx /apps/logs/wbdesigner


# Web app file structure
mkdir /apps
chmod 777 /apps
mkdir /apps/logs
mkdir /apps/logs/wbdesigner
mkdir /apps/logs/wbdesigner/app_log
# chmod 777 /apps/logs/weather_api
cd /apps

# Create a virtual env for the app.
# Make sure pyenv is installed and correct version in 'local'
cd /apps/wbdesigner
poetry shell

# clone the repo:
cd /apps
git clone https://github.com/drewzamcp/pdm_project_one.git wbdesigner

# Setup the web app:
cd /apps/wbdesigner/
poetry install --no-dev

# Copy and enable the daemon
cp /apps/wbdesigner/server/units/wbdesigner.service /etc/systemd/system/

systemctl start wbdesigner
systemctl status wbdesigner
systemctl enable wbdesigner

# Setup the public facing server (NGINX)
apt install nginx

# CAREFUL HERE. If you are using default, maybe skip this
rm /etc/nginx/sites-enabled/default

cp /apps/wbdesigner/server/nginx/wbdesigner.nginx /etc/nginx/sites-enabled/
update-rc.d nginx enable
service nginx restart


# Optionally add SSL support via Let's Encrypt:
# https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04

add-apt-repository ppa:certbot/certbot
apt install python3-certbot-nginx
certbot --nginx -d wbdesigner.com