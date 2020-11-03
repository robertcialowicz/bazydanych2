#!/bin/bash

sleep 20 && sqlcmd -S localhost -U SA -P Sasin70mln -i /usr/share/instnwnd.sql &
/opt/mssql/bin/sqlservr