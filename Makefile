PYTHON := .venv/bin/python
PIP := .venv/bin/pip
MANAGE := $(PYTHON) manage.py
PORT ?= 8080

.PHONY: setup install test check run ci-local health logs

setup:
	python3 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

install:
	$(PIP) install -r requirements.txt

test:
	$(MANAGE) test

check:
	$(MANAGE) check

run:
	$(MANAGE) runserver $(PORT)

ci-local:
	bash scripts/ci_local.sh

health:
	curl -i http://127.0.0.1:$(PORT)/healthz/

logs:
	journalctl -u taskmanager -f
