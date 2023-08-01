FROM python:3.11-buster

WORKDIR /code

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install --upgrade pip
RUN pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile

RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords

COPY . /code/

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
