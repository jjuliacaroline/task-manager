#!/usr/bin/env bash
set -euo pipefail

source .venv/bin/activate
python manage.py check
python manage.py test

echo "Local CI checks passed."
