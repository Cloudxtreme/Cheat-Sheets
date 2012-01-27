# install ssh server
sudo apt-get install openssh-server
netstat -tulpn
vi /etc/ssh/sshd_config
/etc/init.d/ssh restart

#####################################
# Run command on ssh (Secure SHell) # 
#####################################
ssh $user@$host command # sshcom

#Run GUI command on $HOSTNAME as $USER		 
ssh -f -Y $USER@$HOSTNAME xeyes 

#Copy with permissions to $USER's home directory on $HOST
scp -p -r $USER@$HOST: file dir/ 

#Forward connections to $HOSTNAME:8080 out to $HOST:80
ssh -g -L 8080:localhost:80 root@$HOST

#Forward connections from $HOST:1434 in to imap:143
ssh -R 1434:imap:143 root@$HOST