FROM python:3.11-buster

WORKDIR /code

COPY Pipfile .
COPY Pipfile.lock .

RUN apt-get update
RUN apt-get install -y poppler-utils \ 
    tesseract-ocr

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install
RUN pipenv run python -m nltk.downloader punkt
RUN pipenv run python -m nltk.downloader stopwords
COPY . /code/

EXPOSE 8000
CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
