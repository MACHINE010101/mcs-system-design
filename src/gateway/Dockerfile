FROM python:3.12.5-slim-bullseye

RUN apt-get update && apt install build-essential
RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY . /app

EXPOSE 8080

CMD ["python3", "server.py"]