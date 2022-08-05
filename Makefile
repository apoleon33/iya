run:
	python3 backend/server.py

build:
	cd frontend && npm run build
	cp -r frontend/build/ backend/

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install

production: build
	python3 backend/server.py -p