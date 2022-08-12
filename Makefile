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
	python3 backend/server.py

docker: 
	sudo docker build -t iya .

heroku:
	sudo heroku container:push web --app iyap
	heroku container:release -a iyap web