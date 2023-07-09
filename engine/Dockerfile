FROM python:3.11-buster

WORKDIR /engine

COPY Pipfile .
COPY Pipfile.lock .

RUN apt-get update
RUN apt-get install -y poppler-utils \
    tesseract-ocr

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
COPY . /engine/

ENV PYTHONUNBUFFERED 1
ENV PYTHONUNBUFFERED_LOGGING 1
ENV PYTHONUNBUFFERED_LOGLEVEL INFO
ENV PYTHONUNBUFFERED_LOGFORMAT='%(asctime)s - %(levelname)s - %(message)s'

CMD ["python", "-u",  "parse-engine.py"]
