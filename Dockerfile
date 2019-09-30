FROM alpine:3.10

COPY requirements.txt /tmp/requirements.txt

RUN apk add --no-cache --virtual .build-deps \
    libc6-compat=1.1.22-r3 \
    alpine-sdk=1.0-r0 \
    linux-headers=4.19.36-r0 \
    libffi-dev=3.2.1-r6 \
    python3=3.7.3-r0 \
    python3-dev=3.7.3-r0 \
    nginx=1.16.1-r0 \
    uwsgi=2.0.18-r0 \
    uwsgi-python3=2.0.18-r0 \
    git=2.22.0-r0 \
    supervisor=3.3.5-r0 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install --no-cache-dir -r /tmp/requirements.txt && \
    rm /etc/nginx/conf.d/default.conf && \
    rm -r /root/.cache

RUN apk add -U tzdata
RUN cp /usr/share/zoneinfo/Brazil/East /etc/localtime
RUN mkdir -p /app/log
RUN chmod 777 -R /app/log

COPY conf/nginx.conf /etc/nginx/
COPY conf/flask-site-nginx.conf /etc/nginx/conf.d/
COPY conf/uwsgi.ini /etc/uwsgi/
COPY conf/supervisord.conf /etc/supervisord.conf

COPY . /app
WORKDIR /app

CMD ["supervisord"]
