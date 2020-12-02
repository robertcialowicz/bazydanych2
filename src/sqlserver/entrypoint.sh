#!/bin/bash

/opt/mssql/bin/sqlservr &

sleep 10 && /usr/share/import-northwind.sh

tail -f /dev/random &> /dev/null