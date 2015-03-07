# Dependencies 
sudo apt-get install python-setuptools python-dev build-essential 
sudo apt-get install curl  #libcurl3-dev 
sudo apt-get install python-psycopg2
sudo easy_install -U pip
sudo pip install -U virtualenv

# using the virtual_env:
virtualenv virtual_env --no-site-packages
cd virtual_env
source bin/activate

# installing PIL usually: "sudo pip install pil" but in virtual_env:
sudo apt-get install python-imaging
sudo apt-get install libjpeg libjpeg-dev
easy_install -f http://dist.plone.org/thirdparty/ -U PIL==1.1.7

# Install MySQL module usually: "sudo pip install MySQL-python" but in virtual_env:
sudo aptitude install libmysqlclient-dev mysql-server
easy_install http://downloads.sourceforge.net/project/mysql-python/mysql-python-test/1.2.3c1/MySQL-python-1.2.3c1.tar.gz?use_mirror=voxel

# installing other python modules
pip install -E __env__ psycopg2
pip install -E __env__ yolk
pip install -E __env__ django-social-auth
pip install -E __env__ pycurl
Django==1.3
MySQL-python==1.2.3c1
PIL==1.1.7
South==0.7.3
django-debug-toolbar==0.8.5
django-extensions==0.6
django-filter==0.5.3
django-registration==0.7
django-social-auth==0.4.1
django-tagging==0.3.1
django-taggit==0.9.3
httplib2==0.7.1
oauth2==1.5.170
pycurl==7.19.0
python-openid==2.2.5
sorl-thumbnail==11.05.2
wsgiref==0.1.2
django-social-auth

####################################################
##################### mod_wsgi #####################
####################################################
sudo apt-get install libapache2-mod-wsgi
sudo a2enmod mod-wsgi #wsgi
sudo /etc/init.d/apache2 restart

### native installation in bitnami
/etc/ld.so.conf.d/libc.conf # add lib-dir /opt/bitnami/common/lib
sudo ldconfig				# update lib-dir in operative system
sudo ./configure --with-apxs=/opt/bitnami/apache2/bin/apxs
make
sudo make install
LoadModule wsgi_module modules/mod_wsgi.so #in httpd.conf
sudo /opt/bitnami/apache2/scripts/ctl.sh start

# python virtual_env
WSGIPythonHome /home/bitnami/dev/cardgen/cardgen_env

<VirtualHost *:80>
	...
	
	# django config
	<Directory /home/bitnami/dev/cardgen/src/cardgen>
		Order deny,allow
		Allow from all
	</Directory>
	WSGIScriptAlias / /home/bitnami/dev/cardgen/src/cardgen/wsgi_handler.py

	# static files config
	<Directory /home/bitnami/dev/cardgen/src/cardgen/static>
		Order deny,allow
		Allow from all
	</Directory>
	Alias /static/ /home/bitnami/dev/cardgen/src/cardgen/static/

	# process config (optional)
    WSGIDaemonProcess __project__ user=you group=you processes=1 threads=10
    WSGIProcessGroup __project__

    ...
</VirtualHost>

### wsgi_handler.py
import os, sys, site

site.addsitedir('/home/bitnami/dev/cardgen/cardgen_env/lib/python2.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cardgen.settings'
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


####################################################
#################### mod_python ####################
####################################################

# /srv/SaltyCrane/myvirtualdjango.py
activate_this = "/srv/python-environments/saltycrane/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

from django.core.handlers.modpython import handler

# httpd.conf
<Location "/">
	SetHandler python-program
	PythonHandler myvirtualdjango
	SetEnv DJANGO_SETTINGS_MODULE iwiwdsmi.settings
	PythonPath "['/srv/SaltyCrane',] + sys.path"
	PythonDebug Off
</Location>

####################################################
###################### FastCGI #####################
####################################################


####################################################
#################### social auth ####################
####################################################
pip install -E cardgen_env\ django-social-auth
