FROM python:latest
COPY . /server/
RUN pip3 install -r ./server/requirements.txt
WORKDIR /server