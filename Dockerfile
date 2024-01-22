FROM python:3.11-alpine
MAINTAINER Rafal Paciorek

ENV PATH="/scripts:${PATH}"

COPY rent_flat/requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN apk del .tmp

RUN mkdir /rent_flat
COPY rent_flat /rent_flat
WORKDIR /rent_flat
COPY scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

USER user

EXPOSE 8000

CMD ["entrypoint.sh"]