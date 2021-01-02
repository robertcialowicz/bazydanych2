#!/bin/bash

sql=$(sqlcmd -S localhost -U SA -P P@ssword1 -Q "SELECT COUNT(*) FROM Northwind.INFORMATION_SCHEMA.TABLES")
imported=$(echo $sql | grep "Invalid" | wc -l)

if [ $imported -eq 1 ]; then
    echo '>>> importing northwind'
    sqlcmd -S localhost -U SA -P P@ssword1 -i /usr/share/instnwnd.sql
    echo '>>> applying fix to DB to be compatible with django'
    sqlcmd -S localhost -U SA -P P@ssword1 -i /usr/share/dbFix.sql
    echo '>>> northwind imported'
else
    echo '>>> northwind imported previously, skipping'
    echo '>>> applying fix to DB to be compatible with django'
    sqlcmd -S localhost -U SA -P P@ssword1 -i /usr/share/dbFix.sql
fi