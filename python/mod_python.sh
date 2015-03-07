PYTHONPATH variable is set to

echo $PYTHONPATH
/root/djangoprojects/mysite

DJANGO_SETTINGS_MODULE is set to

echo $DJANGO_SETTINGS_MODULE
mysite.settings

<Location "/mysite">
    SetHandler python-program
    PythonHandler django.core.handlers.modpython
    SetEnv DJANGO_SETTINGS_MODULE mysite.settings
    PythonOption django.root /mysite
    PythonPath "['/root/djangoprojects/', '/root/djangoprojects/mysite','/root/djangoprojects/mysite/polls', '/var/www'] + sys.path"
    PythonDebug On
</Location>



SetEnv DJANGO_SETTINGS_MODULE acecoach.settings