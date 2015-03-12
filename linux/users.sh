# Ubuntu # adduser <username>
sudo useradd -s /bin/bash -d /home/bitnami -m bitnami
sudo useradd -s /bin/bash -d /home/djuser -m djuser
sudo passwd bitnami
groupadd -r grupo
gpasswd -a usuario grupo
# freedomM0dF3r21.

#lista de usuario
sudo cat /etc/shadow

#usuarios conectados
users
cat /etc/passwd | grep ftp

#activar y desactivar root en ubuntu
sudo passwd root
sudo passwd -l root
