FROM alpine

COPY requirements.txt /tmp/requirements.txt

ENV FILEBEAT_VERSION=6.1.1

RUN apk add --no-cache \
    libc6-compat \
    python3 \
    bash \
    nginx \
    uwsgi \
    git \
    uwsgi-python3 \
    supervisor && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install six && \
    pip3 install mock && \
    pip3 install -r /tmp/requirements.txt && \
    rm /etc/nginx/conf.d/default.conf && \
    rm -r /root/.cache

RUN apk add -U tzdata
RUN cp /usr/share/zoneinfo/Brazil/East /etc/localtime
RUN mkdir -p /var/log/app/
RUN chmod 777 -R /var/log/app/

COPY conf/nginx.conf /etc/nginx/

COPY conf/flask-site-nginx.conf /etc/nginx/conf.d/

COPY conf/uwsgi.ini /etc/uwsgi/

COPY conf/supervisord.conf /etc/supervisord.conf

COPY . /app
WORKDIR /app

CMD ["supervisord"]
