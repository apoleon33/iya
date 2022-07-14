run:
	python3 backend/server.py

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install