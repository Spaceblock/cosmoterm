FROM ubuntu:latest
MAINTAINER mb6ockatf 'mdddmmmm@ya.ru'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ['python3']
CMD ['src/app.py', 'random_stuff']