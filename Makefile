install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C add.py
test:
	python -m pytest -vv test_add.py

run:
	streamlit run App.py