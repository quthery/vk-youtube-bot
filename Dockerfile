FROM python:3.12

WORKDIR /bot

COPY req.txt req.txt

RUN pip3 install -r req.txt

RUN apt-get -y update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN chmod 755 .
COPY . .

CMD [ "python3", "run.py"]
