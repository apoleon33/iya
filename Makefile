run:
	python3 backend/server.py -l

build:
	cd frontend && npm run build
	cp -r frontend/build/ backend/

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install

convert:
	python3 backend/converter.py

production: build convert
	cd backend && gunicorn --bind 0.0.0.0:3033 server:app

docker:
	sudo systemctl start docker
	sudo docker build -t iya .

heroku:
	sudo systemctl start docker
	sudo heroku container:push web --app iyap
	heroku container:release -a iyap web