all:scss run

run: 
	python3 backend/server.py & cd frontend && npm start

scss:
	sass static/style.scss static/style.css

install: scss
	pip install -r requirements.txt