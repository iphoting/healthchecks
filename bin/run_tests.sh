#!/usr/bin/env bash

echo "Running tests..."
coverage run --omit=*/tests/* --source=hc manage.py test
