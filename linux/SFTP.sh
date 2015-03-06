# ssh-keygen -t rsa
# scp /home/Usuario/.ssh/id_rsa.pub root@192.168.2.67:.ssh/authorized_keys

sftp root@192.168.2.67 << EOT
lcd /export/home/data/respaldo_SP_TT/SS2/TT
cd /home/mauro
bye
quit
EOT