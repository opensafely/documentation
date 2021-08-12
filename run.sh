#!/bin/sh -e
docker build -t docs . && docker run --rm -p 127.0.0.1:8000:8000 --volume "${PWD}":/home/dockeruser/app docs
