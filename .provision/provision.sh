#!/usr/bin/bash

#Upgrade python
sudo apt update
sudo apt -yqq install python3-venv

#Activate virtual environment
sudo python3 -m venv venv
source /vagrant/venv/bin/activate

#install packages
pip install markdown django==4.0.3 djangorestframework django-filter psycopg2-binary django-environ django-cors-headers httpie

#deactivate the venv
deactivate


