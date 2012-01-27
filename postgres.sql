createdb test
psql test
CREATE ROLE testuser WITH SUPERUSER LOGIN PASSWORD 'testpass';
CREATE ROLE satchmo WITH SUPERUSER LOGIN PASSWORD 'satchmo12';
-- CREATE DATABASE database OWNER role;
-- createdb -O rolename dbname
