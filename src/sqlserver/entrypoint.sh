#!/bin/bash

sleep 30 && sqlcmd -S localhost -U SA -P Sasin70mln -i /usr/share/instnwnd.sql &
/opt/mssql/bin/sqlservr