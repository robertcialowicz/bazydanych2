#!/bin/bash

docker rm -f sql-server && docker build -t sql-server:2019 . && docker run -d --name sql-server -v "$(pwd)/sql-server-data:/opt/sql-server-data" sql-server:2019
