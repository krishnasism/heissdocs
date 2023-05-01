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

CMD ["python", "-u",  "parse-engine.py"]
