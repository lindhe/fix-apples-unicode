all: init

MAIN_FILE = ./checkfiles.py

init:
	pipenv install --dev

install:
	install $(MAIN_FILE) /usr/local/bin/svenska
