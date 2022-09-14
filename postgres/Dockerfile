FROM postgres

ENV POSTGRES_PASSWORD pgpassword

COPY init-script.sql /docker-entrypoint-initdb.d/
COPY init-permissions.sh /docker-entrypoint-initdb.d/
COPY postgresql.conf /etc/postgresql.conf