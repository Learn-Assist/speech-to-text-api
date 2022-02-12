FROM python:3.8.0-slim

WORKDIR /flask-production

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apt-get -y update

RUN apt-get install -y ffmpeg

COPY . /flask-production/

EXPOSE 3005

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0" ]