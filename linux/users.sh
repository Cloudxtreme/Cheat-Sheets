# Ubuntu # adduser <username>
sudo useradd -s /bin/bash -d /home/djuser -m djuser
sudo passwd djuser
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

#add to sudoers
sudo adduser djuser sudo
