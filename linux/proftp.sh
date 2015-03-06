apt-get install proftpd
echo "/bin/false" >> /etc/shells
mkdir /home/FTP-public
useradd userftp -p ftppass -d /home/FTP-public -s /bin/false

sudo mkdir /home/FTP-public/download
sudo mkdir /home/FTP-public/upload
sudo chmod 755 /home/FTP-public
sudo chmod 755 /home/FTP-public/download
sudo chmod 777 /home/FTP-public/upload

vim /etc/proftpd/proftpd.conf
# AllowOverwrite on
# AuthAliasOnly on
# UserAlias vensign userftp

/etc/init.d/proftpd restart