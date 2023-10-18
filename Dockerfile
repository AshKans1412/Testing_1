FROM python:3.9.1

WORKDIR /app

COPY pipeline_v2.py pipeline_v2.py

COPY secrets.env secrets.env

RUN pip install pandas sqlalchemy psycopg2 python-dotenv

ENTRYPOINT [ "python", "pipeline_v2.py" ]