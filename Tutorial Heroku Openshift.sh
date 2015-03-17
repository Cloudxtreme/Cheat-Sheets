xexo19
http://www.descargatelocorp.com
KEVIN2009K
http://hypem.com/download/B/

 cd myapp
 git init

Heroku tricks
# Crear app en heroku

# download git
git clone xxxxx

# upload
git add .
git commit . -m "primer post"
git push origin master  #git push heroku master

# NOTA: tienes que tener index.php
# base de datos
heroku addons:add heroku-postgresql

# go to website heroku so you can read heroku configuration
# connect externally
ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory

# Database configuration Codeigniter PHP
$url = parse_url(getenv("DATABASE_URL"));
$db['default']['hostname'] = $url["host"];
$db['default']['username'] = $url["user"];
$db['default']['password'] = $url["pass"];
$db['default']['database'] = substr($url["path"], 1);
$db['default']['port'] = "5432";
$db['default']['dbdriver'] = 'postgre';

# https://devcenter.heroku.com/articles/custom-php-settings
# https://devcenter.heroku.com/articles/php-support

########################################################################
# Custom Domains OpenShift
# https://access.redhat.com/documentation/en-US/OpenShift_Online/2.0/html/User_Guide/sect-Custom_Domains_and_SSL_Certificates.html
rhc alias add App_Name Custom_Domain_Name
rhc alias list App_Name
rhc alias remove App_Name Custom_Domain_Name


  Root User: adminRClxlve
   Root Password: klwsmw377fza
   Database Name: php

Connection URL: mysql://$OPENSHIFT_MYSQL_DB_HOST:$OPENSHIFT_MYSQL_DB_PORT/