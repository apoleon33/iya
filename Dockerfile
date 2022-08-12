FROM python:3.8

WORKDIR /

COPY . .

RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip nodejs npm make
RUN make install
RUN make build
RUN make convert

EXPOSE 5000

CMD cd backend && gunicorn --bind 0.0.0.0:3033 main:app --timeout 600
