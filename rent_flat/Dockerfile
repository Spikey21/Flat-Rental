FROM python:3.11
MAINTAINER Rafal Paciorek

ENV PYTHONUNBUFFERED=1

COPY ../requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . /rent_flat
WORKDIR /rent_flat

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]