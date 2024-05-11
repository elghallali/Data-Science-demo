install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test/test_*.py

format:
	black *.py mylib

lint:
	pylint --disable=R,C *.py

all: install lint test
