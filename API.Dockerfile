FROM python:3.12

COPY ./src /weatherapp
COPY .env /weatherapp/.env
COPY requirements.txt /weatherapp/requirements.txt

WORKDIR /weatherapp

RUN pip install -r requirements.txt

CMD [ "python", "/weatherapp/main.py" ]
