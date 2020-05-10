FROM alpine:3.10

RUN apk add --no-cache --virtual .build-deps \
    alpine-sdk \
    git \
    libc6-compat \
    libffi-dev \
    linux-headers \
    nginx \
    python3-dev \
    supervisor \
    tzdata \
    uwsgi-python3 \
    uwsgi

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install --upgrade pip==19.2.3 setuptools==41.4.0 && \
    pip3 install --no-cache-dir -r /tmp/requirements.txt && \
    rm /etc/nginx/conf.d/default.conf && \
    rm -r /root/.cache

COPY conf/nginx.conf /etc/nginx/
COPY conf/flask-site-nginx.conf /etc/nginx/conf.d/
COPY conf/uwsgi.ini /etc/uwsgi/
COPY conf/supervisord.conf /etc/supervisord.conf

COPY . /app
WORKDIR /app

CMD ["supervisord"]
