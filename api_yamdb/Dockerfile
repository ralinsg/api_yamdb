FROM python:3.7-slim

LABEL author="ralinsg" version='0.1' release_date='15.11.2022'

WORKDIR /app

COPY ./ requirements.txt/ /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
