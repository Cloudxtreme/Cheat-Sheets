/usr/local/bin/rsync --no-detach --daemon --config /etc/rsyncd.conf &

/var/www/html/fer/joomweb

Step-by-step installation and configuration rsync server on CentOS
From transamrit.net

    * Make sure xinetd and rsync is available, if not type
      # yum -y install rsync xinetd
    * Add xinetd service to system
      # chkconfig --add xinetd
    * Make sure xinetd running on init 3 and 5
      # chkconfig --list xinetd
    * Enable rsync
      # vi /etc/xinetd.d/rsync
      Change disable = yes into disable = no
    * Create username and password for rsync client to use
      # vi /etc/rsyncd.secrets
      adminname:hispassword
    * Create configuration and shares for rsync daemon
      # vi /etc/rsyncd.conf
      max connections = 2
      log file = /var/log/rsync.log
      timeout = 300

      [shares]
      comment = shared data stored here
      path = /home/adminname/shares
      read only = false # chg to true if you want read only
      list = yes
      uid = adminname
      gid = adminname
      auth users = adminname
      secrets file = /etc/rsyncd.secrets
      hosts allow = 10.10.105.0/24
      
      ##########################
      [web]
        path = /var/www/html/fer/joomweb
        read only = no
        uid = fernando      
      ##########################
      
      
    * Secure /etc/rsyncd.*
      # chown root.root /etc/rsyncd.*
      # chmod 600 /etc/rsyncd.*
    * Restart xinetd
      # service xinetd restart
    * Make sure rsync now running
      # chkconfig --list
    * Perhaps you also want to enable port 873 tcp and udp on your 
    firewall so other can connect to your server