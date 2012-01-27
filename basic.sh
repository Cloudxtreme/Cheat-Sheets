# Ubuntu # adduser <username>
sudo useradd -s /bin/bash -d /home/bitnami -m bitnami
sudo passwd bitnami
groupadd -r grupo
gpasswd -a usuario grupo

#lista de usuario
sudo cat /etc/shadow
users #usuarios conectados
cat /etc/passwd | grep ftp

#activar y desactivar root en ubuntu
sudo passwd root
sudo passwd -l root

# Compresion de archivos
tar -zcvf file.tar.gz file1 file2 ... dir1 dir2 ...
tar -zxvf file.tar.gz
tar -zxvf file.tar.gz -C /tmp/extractHere/

# add shared library
vi /etc/ld.so.conf
vi /etc/ld.so.conf.d/libc.conf
sudo ldconfig

ratoncita_parati@
