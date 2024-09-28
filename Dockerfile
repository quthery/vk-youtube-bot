FROM python:3.12

WORKDIR /bot

COPY req.txt req.txt

RUN pip3 install -r req.txt

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

RUN chmod 755 .
COPY . .

CMD [ "python3", "run.py"]
