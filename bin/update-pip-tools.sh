#!/usr/bin/env bash

echo "Installing/Updating virtualenvwrapper..."
pip3 install -U virtualenvwrapper
source `which virtualenvwrapper.sh`

VENV=`cat .venv`
echo "Activating ${VENV:-healthchecks-heroku} venv..."
if ! workon ${VENV:-healthchecks-heroku}; then
    echo "Building venv ${VENV:-healthchecks-heroku}..."
    mkvirtualenv ${VENV:-healthchecks-heroku} -r requirements-dev.txt -i virtualenvwrapper
fi

echo "Updating venv dev packages..."
pip install -U pip
pip install -U -r requirements-dev.txt

echo "Updating project packages..."
pip-compile --upgrade --generate-hashes
pipenv lock

echo "Syncing venv with latest project packages..."
pip-sync ; pip install -r requirements-dev.txt

## test
echo "Starting webserver..."
honcho start web

echo "Exiting venv..."
deactivate

echo "Done."
