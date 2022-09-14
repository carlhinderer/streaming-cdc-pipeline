CREATE DATABASE retaildb;
CREATE USER retailuser WITH PASSWORD 'retailpw';
GRANT ALL PRIVILEGES ON DATABASE retaildb TO retailuser;

-- Replication settings for Debezium
ALTER ROLE "retailuser" WITH LOGIN REPLICATION SUPERUSER;