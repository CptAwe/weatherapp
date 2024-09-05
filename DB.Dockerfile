FROM mysql:9.0

COPY DB.sql /docker-entrypoint-initdb.d/init.sql
