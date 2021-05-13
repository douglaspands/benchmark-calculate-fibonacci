FROM python:3.9.5-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./

EXPOSE 8080
CMD [ "waitress-serve", "--call", "app:create_app" ]