#Create a ubuntu base image with python 3 installed.
FROM python:3.8

#Set the working directory
WORKDIR /

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip nodejs npm make
RUN make install
RUN make build
RUN make convert

#Expose the required port
EXPOSE 5000

#Run the command
CMD cd backend && gunicorn --bind 0.0.0.0:3033 main:app --timeout 600
