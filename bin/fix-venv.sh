#!/usr/bin/env bash

# to fix broken venv due to Homebrew python upgrades

VENV=`cat .venv`
if [ "${WORKON_HOME}" -a -d "${WORKON_HOME}" ]; then
	find -L "${WORKON_HOME}/${VENV:-healthchecks-heroku}" -type l | xargs rm
	virtualenv "${WORKON_HOME}/${VENV:-healthchecks-heroku}"
fi
