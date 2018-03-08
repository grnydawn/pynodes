# This Makefile assumens that it is executed in virtualenv

PWD = $(shell pwd)

test: FORCE
	export PYTHONPATH=${PWD}:${PYTHONPATH}; pytest

lint:
	pylint pynodes

install:
	python setup.py install --user --record installed_files.txt

uninstall:
	cat installed_files.txt | xargs rm -rf
	rm -f installed_files.txt

setup:
	pip install -r requirements.txt

gendoc:

clean:

FORCE:
