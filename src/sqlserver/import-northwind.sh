#!/bin/bash

sql=$(sqlcmd -S localhost -U SA -P Sasin70mln -Q "SELECT COUNT(*) FROM Northwind.INFORMATION_SCHEMA.TABLES")
imported=$(echo $sql | grep "Invalid" | wc -l)

if [ $imported -eq 1 ]; then
    echo '>>> importing northwind'
    sqlcmd -S localhost -U SA -P Sasin70mln -i /usr/share/instnwnd.sql
    echo '>>> northwind imported'
else
    echo '>>> northwind imported previously, skipping'
fi