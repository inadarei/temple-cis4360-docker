#!/bin/bash

docker run -p 127.0.0.1:8181:8000/tcp --rm \
       --name cis4360-python-hello -t cis4360-python-hello:latest