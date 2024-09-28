FROM python:3.12

WORKDIR /bot

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

RUN chmod 755 .
COPY . .

CMD [ "python3", "run.py"]
