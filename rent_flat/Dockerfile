FROM python:3.11
MAINTAINER Rafal Paciorek

ENV PYTHONUNBUFFERED=1

COPY ../requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /rent_flat
COPY ./rent_flat /rent_flat

RUN adduser -D user

EXPOSE 8000

ENTRYPOINT ["python", "rent_flat/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]