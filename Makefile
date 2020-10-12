
all: init

init:
	pipenv install --dev

install:
	install ./checkfiles.py /usr/local/bin/svenska
