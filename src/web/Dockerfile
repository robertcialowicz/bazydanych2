FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/

##############################
#install db driver and tools #
##############################
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools
RUN apt-get -y install unixodbc unixodbc-dev
RUN apt-get install nano
############################
#Create symlinks for tools #
############################
RUN ln -sfn /opt/mssql-tools/bin/sqlcmd /usr/bin/sqlcmd 
RUN ln -sfn /opt/mssql-tools/bin/bcp /usr/bin/bcp

#######################
#install requirements #
#######################
RUN pip install -r /code/requirements.txt
COPY . /code/

CMD python manage.py migrate
CMD python manage.py createsuperuser --username admin --password admin --noinput --email 'admin@email.com'

CMD python /code/test.py