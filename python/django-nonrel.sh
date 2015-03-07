hg clone https://iwxfer@bitbucket.org/wkornewald/django-nonrel
hg clone https://iwxfer@bitbucket.org/wkornewald/djangoappengine
hg clone https://iwxfer@bitbucket.org/wkornewald/djangotoolbox
hg clone https://iwxfer@bitbucket.org/twanschik/django-autoload
hg clone https://iwxfer@bitbucket.org/wkornewald/django-dbindexer
hg clone https://iwxfer@bitbucket.org/wkornewald/django-testapp

    * <project>/django
    * <project>/djangotoolbox
    * <project>/autoload
    * <project>/dbindexer
    * <project>/djangoappengine

	manage.py createsuperuser 
	
	    * manage.py remote allows you to execute a command on the production database (e.g., manage.py remote shell or manage.py remote createsuperuser)
    * manage.py deploy uploads your project to App Engine (use this instead of appcfg.py update)

	itionally djangotoolbox provides non-Django field types in djangotoolbox.fields which you can use on App Engine or other non-relational databases. These are

    * ListField
    * BlobField

	he following App Engine properties can be emulated by using a CharField in Django-nonrel:

    * CategoryProperty
    * LinkProperty
    * EmailProperty
    * IMProperty
    * PhoneNumberProperty
    * PostalAddressProperty
