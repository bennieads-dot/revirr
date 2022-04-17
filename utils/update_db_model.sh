#! /usr/bin/bash

cd /vagrant/revirr_root

echo "Creating migrations"
python manage.py makemigrations

retVal=$?

if [ $retVal -ne 0 ]; then
    echo "ERROR when creating DB migrations"
    exit $retVal
fi

echo "Migrations created, sending changes to the database"

python manage.py migrate

retVal=$?

if [ $retVal -ne 0 ]; then
    echo "ERROR when creating DB migrations"
    exit $retVal
fi

echo "Data model updated successfully"

exit $retVal