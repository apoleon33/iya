all:scss run

run: 
	python3 server.py

scss:
	sass static/style.scss static/style.css

install: scss
	pip install -r requirements.txt