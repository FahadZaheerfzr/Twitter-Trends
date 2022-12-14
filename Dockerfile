# Dockerfile, Image, Container

FROM python:3.8.5

WORKDIR /getting_started

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD [ "python3", "./app/main.py" ]