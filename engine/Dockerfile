FROM python:3.11-buster

WORKDIR /engine


RUN pip install --upgrade pip
RUN pip install boto3
RUN pip install requests
COPY . /engine/

CMD ["python", "-u",  "parse-engine.py"]
