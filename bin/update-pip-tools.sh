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
pip-compile --upgrade
pip-compile --upgrade requirements-dev.in
#pip-compile --upgrade --generate-hashes
#pip-compile --upgrade --generate-hashes requirements-dev.in
pip-compile --upgrade requirements-tests.in
pipenv lock

echo "Syncing venv with latest project packages..."
# workaround -lssl errors on macos venv when building psycopg2
export LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib"
pip-sync  requirements.txt requirements-dev.txt requirements-tests.txt

## test
#echo "Starting webserver..."
#honcho start web

echo "Starting tests..."
coverage run --omit=*/tests/* --source=hc manage.py test

echo "Exiting venv..."
deactivate

echo "Done."
