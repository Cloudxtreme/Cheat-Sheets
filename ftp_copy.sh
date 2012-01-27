hostname="myhost"  
username="user"  
password="pass"  

ftp -n $hostname <<EOF  
quote USER $username  
quote PASS $password  
binary  
lcd /home/pages  
cd /www/pages  
mput *.html  
quit  
EOF
