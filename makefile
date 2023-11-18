#!/usr/bin/make -f

run:
	python3 src/app.py random_stuff

build:
	python3 -m venv venv
	. venv/bin/activate
	python3 -m pip install -r requirements.txt
	npm install package.json
