FROM python:3.12-alpine

WORKDIR /bot

COPY req.txt req.txt

RUN pip3 install -r req.txt

RUN apk add --no-cache ffmpeg libsm-dev libxrender libxext-dev 
RUN chmod 755 .
COPY . .

CMD [ "python3", "run.py"]
