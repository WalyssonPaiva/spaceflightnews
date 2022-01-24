# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster as base

WORKDIR /home

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x run

FROM base as test 
RUN ["./run", "tests"]

FROM base as development
EXPOSE 8000
CMD ["uvicorn", "lib.app:app", "--host", "0.0.0.0", "--port", "8000"]