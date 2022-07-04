all: back front

back: 
	python3 backend/server.py

front:
	cd frontend && npm start

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install