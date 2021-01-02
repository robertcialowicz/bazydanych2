FROM mcr.microsoft.com/mssql/server:2019-latest


########################
# Configure SQL Server #
########################

ARG SQL_PASSWD="P@ssword1"
ENV ACCEPT_EULA="Y"
ENV SA_PASSWORD="${SQL_PASSWD}"
ENV MSSQL_PID="Express"

ENV PATH=$PATH:/opt/mssql-tools/bin

WORKDIR "/"

########################
# Setup Northwind Data #
########################

ARG NORTHWIND_SQL_GITHUB="https://raw.githubusercontent.com/Microsoft/sql-server-samples/master/samples/databases/northwind-pubs/instnwnd.sql"
ARG NORTHWIND_SQL="/usr/share/instnwnd.sql"
RUN wget "${NORTHWIND_SQL_GITHUB}" -O "${NORTHWIND_SQL}"
ADD entrypoint.sh /usr/share/entrypoint.sh
ADD import-northwind.sh /usr/share/import-northwind.sh
ADD dbFix.sql usr/share/dbFix.sql
ENTRYPOINT [ "/usr/share/entrypoint.sh" ]