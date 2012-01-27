#!/bin/bash
 
## BEGIN CONFIG ##
HOST=localhost
USER=usuario
PASS=secreto
BACKUP_DIR=Backup
## END CONFIG ##
 
if [ ! -d $BACKUP_DIR ]; then
  mkdir -p $BACKUP_DIR
fi
 
# Backup de MySQL
MYSQL_DBS=$(mysqlshow -h $HOST -u $USER -p$PASS | awk ' (NR > 2) && (/[a-zA-Z0-9]+[ ]+[|]/) && ( $0 !~ /mysql/) { print $2 }');
 
for DB in $MYSQL_DBS ; do 
  echo "* Backuping MySQL data from $DB@$HOST..."
  mysqldump -h $HOST -u $USER -p$PASS $DB > $BACKUP_DIR/mysql_$DB.sql
done