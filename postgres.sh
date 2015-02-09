# Install postgres 8.4
sudo aptitude install postgresql-8.4 postgresql-client-8.4 pgadmin3
sudo /etc/init.d/postgresql-8.4 start

# Set 'postgres' password and create first database and user
sudo passwd postgres
su postgres

# By default Postgresql uses IDENT-based authentication. All you have to do is allow username and password based authentication for your network or webserver. IDENT will never allow you to login via -U and -W options. 
#	local	all	all	            trust
#	host	all	127.0.0.1/32	trust

# Finally for connect to the database:
psql database -U user -W
psql satchmostore -U satchmo -W

# Para poder acceder de forma remota
/etc/postgresql/8.4/main/postgresql.conf
	#listen_addresses = 'localhost' --> listen_addresses = '*' o listen_addresses = '0.0.0.0'
	#password_encryption = on --> password_encryption = on 

# configurar la lista de acceso 
/etc/postgresql/8.4/main/pg_hba.conf
host all all 192.168.1.4 255.255.255.0 md5 
# acceso sin usuario ni password: 
host all all 192.168.1.4 255.255.255.0 md5 
# desde cualquier IP
host all all 0.0.0.0 0.0.0.0 md5
# un usuario especifico desde IP especifica
host MyDataBase MyUser 192.168.1.4 255.255.255.0 md5

# gestion de usuarios
createuser -A -d -P -h host -U new_user
dropuser -h host -U user

# Backup full database
pg_dump -h host -U user -W database > backup.sql

# Restore
psql -d database -f backup.sql

# Retore from compressed dump
pg_restore -U postgres -W -h 127.0.0.1 -d database database.backup

# Backup database schema
pg_dump -sv prueba -O > backup.schema.sql

# Backup database data
pg_dump -Fc -f backup.data.dump -a --disable-triggers database

############### utiles #############
\dg : list roles and groups
\dt : list of tables
