FROM python:3.7-alpine
MAINTAINER Irakli Nadareishvili

COPY . /app
WORKDIR /app

RUN apk upgrade --update \
 && apk add --no-cache build-base \
 && apk add bash \
 && pip install -r requirements.txt

CMD ["gunicorn", "-b 0.0.0.0", "--reload", "-w 4", "server:app"]

# Build:
# docker build -t cis4360-python-hello:latest .

# Run:
# docker run -p 127.0.0.1:8181:8000/tcp --rm -t cis4360-python-hello:latest

# Debug:
# docker run -it cis4360-python-hello:latest sh
# or
# docker run -it cis4360-python-hello:latest bash