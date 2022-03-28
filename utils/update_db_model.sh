#! /usr/bin/bash

cd /revirr/revirr

echo "Creating migrations"
python manage.py makemigrations api

retVal=$?

if [ $retVal -ne 0 ]; then
    echo "ERROR when creating DB migrations"
    exit $retVal
fi

echo "Migrations created, sending changes to the database"

python manage.py migrate api

retVal=$?

if [ $retVal -ne 0 ]; then
    echo "ERROR when creating DB migrations"
    exit $retVal
fi

echo "Data model updated successfully"

exit $retVal