FROM python:3.8.0-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apt-get -y update
RUN apt-get install -y ffmpeg

COPY . /app/

RUN mkdir audio

CMD ["python3","app.py"]
