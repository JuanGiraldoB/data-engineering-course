FROM python:3.12

RUN apt-get install curl
RUN pip install pandas sqlalchemy pyarrow psycopg2

WORKDIR /app
COPY upload_data.py upload_data.py

ENTRYPOINT [ "python", "upload_data.py" ]