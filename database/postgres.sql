createdb test
psql test
CREATE ROLE testuser WITH SUPERUSER LOGIN PASSWORD 'testpass';
CREATE ROLE satchmo WITH SUPERUSER LOGIN PASSWORD 'satchmo12';
-- CREATE DATABASE database OWNER role;
-- createdb -O rolename dbname

# create user and grant ownership
sudo -u postgres psql -c "CREATE USER __USER__ WITH PASSWORD '__PASS__';"
sudo -u postgres psql -c "CREATE DATABASE __DATABASE__ WITH OWNER fer ENCODING 'utf-8';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE __DATABASE__ to __USER__;"
# add owner to a database
sudo -u postgres psql -c "ALTER DATABASE __DATABASE__ OWNER TO __USER__;"
