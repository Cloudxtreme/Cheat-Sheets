
# merging with existing repo
git remote add OPENSHIFT_REMOTE_GIT_REPO
git pull openshift master

# My app: servicios

# Adding cron to my app
rhc cartridge add cron-1.4 -a servicios

# servicios/.openshift/cron/minutely
create a file called mycron
	#!/bin/bash
	date >> ${OPENSHIFT_PHP_LOG_DIR}/mycron.log
	
chmod +x mycron 
