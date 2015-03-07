python manage.py runserver 0.0.0.0:8000
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil

python manage.py syncdb 
python manage.py runserver

"""----------------------------------------------------------
    South
   ----------------------------------------------------------"""
python manage.py migrate

# Initial
python manage.py schemamigration __app__ --initial
python manage.py migrate __app__
# Update
python manage.py schemamigration __app__ --auto
python manage.py migrate __app__
# then syncdb
python manage.py migrate __app__ --fake 

# --list: Shows what migrations are available, and puts a * next to ones which have been applied.
# --merge: Runs any missed (out-of-order) migrations without rolling back to them.
# --no-initial-data: Doesn't load in any initial data fixtures after a full upwards migration.
# --fake: Records the migration sequence as having been applied, but doesn't actually run it.
# --db-dry-run: this is useful for sanity-testing migrations to check API calls are correct.


################## Templates ##################
*For and If statements
{{{
{% for object in objects %}
  {% if forloop.first %}
    <li class="first">
  {% else %}
    <li>
  {% endif %}
  {{ object }}
  </li>
{% endfor %}
}}}

*Nice menu example:
{{{
{% for link in links %} {{ link }}
  { % if not forloop.last %} | { % endif %}
{% endfor %}
}}}

*Comparing variables
{% ifequal variable 1 %}
{% ifequal variable 1.23 %}
{% ifequal section "community" %}
{% ifequal section 'sitenews' %}
{% ifequal user currentuser %}
    <h1>Welcome!</h1>
{% else %}
    <h1>No News Here</h1>
{% endifequal %}

*Filters
{{{
{{ name|lower }}    			# lowercase the text
{{ bio|truncatewords:"3" }}  	# words! not characters
addslashes: Agrega una con contra-barra.
date: Formatea un objeto date o datetime {{ pub_date|date:"F j, Y" }}
escape: convierte caracteres especiales a xhtml
}}}
"""----------------------------------------------------------
    Sessiones
----------------------------------------------------------"""
   
# Set a session value:
request.session["color"] = "blue"

# Get a session value -
fav_color = request.session["color"]

# Clear an item from the session:
del request.session["color"]

# Check if the session has a given key:
if "color" in request.session:


################## Render ##################
from django.template import loader, Context

t = loader.get_template('my_template.html')
c = Context({ 'object_list': SomeModel.objects.all() })
rendered = t.render(c)
return HttpResponse(t.render(c))

# another way
return render_to_response('my_template.html', { 'object_list': SomeModel.objects.all() })

# don't want a response
from django.template.loader import render_to_string
email_body = render_to_string("email_template.txt", { 'name': 'Bob', 'message': 'Hello!' })

from django.conf.urls.defaults import *

"""----------------------------------------------------------
    URLconf
----------------------------------------------------------"""

from django.conf.urls.defaults import *    

urlpatterns = patterns('',
    (r'^articles/2003/$',          'news.views.special_case_2003'),
    (r'^articles/(\d{4})/$',       'news.views.year_archive'),
    (r'^articles/(\d{4})/(\d+)/$', 'news.views.month_archive'),
	(r'^user/(?P<username>\w{0,50})/$', 'auth.views.profile',), 
)
/articles/2005/03/ => news.views.month_archive(request, '2005')
/articles/2005/03/ => news.views.month_archive(request, '2005', '3')
/user/theuser/     => auth.views.profile(request, username='username')

urlpatterns = patterns('',
    (r'^articles/(?P<year>\d{4})/$',                'news.views.year_archive'),
    (r'^articles/(?P<year>\d{4})/(?P<month>\d+)/$', 'news.views.month_archive'),
)
/articles/2005/03/    => news.views.month_archive(request, year='2005')
/articles/2003/03/3/  => news.views.article_detail(request, year='2003', month='3')

"""----------------------------------------------------------
    Form Processing
----------------------------------------------------------"""

from django.http import HttpResponse
from django.shortcuts import render_to_response
from mysite.books.models import Book

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return HttpResponse('Please submit a search term.')
	return render_to_response('search_form.html', {'error': True})

"""----------------------------------------------------------"""
<html>
<head>
    <title>Search</title>
</head>
<body>
    {% if error %}
        <p style="color: red;">Please submit a search term.</p>
    {% endif %}
    <form action="/search/" method="get">
        <input type="text" name="q">
        <input type="submit" value="Search">
    </form>
</body>
</html>

"""----------------------------------------------------------"""
<p>You searched for: <strong>{{ query }}</strong></p>
{% if books %}
    <p>Found {{ books|length }} book{{ books|pluralize }}.</p>
    <ul>
        {% for book in books %}
        <li>{{ book.title }}</li>
        {% endfor %}
    </ul>
{% else %}
    <p>No books matched your search criteria.</p>
{% endif %}


"""----------------------------------------------------------
    Web Testing
----------------------------------------------------------"""

from django.test.client import Client

c = Client()
response = c.post('/login/', {'username': 'john', 'password': 'smith'})
response.status_code # will give 200
response = c.get('/customer/details/')
response.content # will display the response

################## Web Debugging ##################
return HttpResponse(str("ok"))
request.META['wsgi.errors'].write("testing")

"""----------------------------------------------------------
    Request Response
----------------------------------------------------------"""

if request.method == 'GET':
    do_something()
elif request.method == 'POST':
    do_something_else()

# Response
response = HttpResponse("Here's the text of the Web page.")
response = HttpResponse("Text only, please.", mimetype="text/plain")

# Response as a file-like object:
response = HttpResponse()
response.write("<p>Here's the text of the Web page.</p>")
response.write("<p>Here's another paragraph.</p>")


"""----------------------------------------------------------
    Models
----------------------------------------------------------"""

class Publisher(models.Model):
  name = models.CharField(maxlength=30, help_text='Name', unique=True)
  address = models.TextField(maxlength=50)
  city = models.CharField(maxlength=60, default='London')

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]

# creating and saving
ringo = Person.objects.create(name="Ringo Starr") 
p1 = Publisher(name='Addison-Wesley', address='75 Arlington Street')
p1.save()

# getting and filtering
publisher_list = Publisher.objects.all()
Publisher.objects.filter(name="Apress Publishing")
Publisher.objects.filter(name__contains="press") # icontains, startswith y, endswith y, range

Publisher.objects.get(name="Apress Publishing") # exception if many objects
Publisher.objects.order_by("name")
Publisher.objects.order_by("-name")
Publisher.objects.order_by("state_provice", "address")

Publisher.objects.filter(country="U.S.A.").order_by("-name")
Publisher.objects.all()[0]  #LIMIT 1

p = Publisher.objects.get(name="Addison-Wesley")
p.delete()
publishers = Publisher.objects.all()
publishers.delete()

for e in Entry.objects.all():
    print e.headline
    
# agregar nuevo campo a tabla existente
campo_nuevo = models.IntegerField(blank=True, null=True)
manage.py sqlall [yourapp] para ver la nueva sentencia CREATE TABLE
ALTER TABLE que agregue tu nueva columna.
en produccion Ejecuta la sentencia ALTER TABLE que se uso antes
Agrega el campo a tu modelo.

# Execute custom SQL
from django.db import transaction, connection
cursor = connection.cursor()
cursor.execute("DELETE FROM cms_cmsplugin WHERE id=%s", [str(plugin.id)])
transaction.commit_unless_managed()

############# Many to Many for form in both classes #############
class ManyToManyField_NoSyncdb(models.ManyToManyField):
    def __init__(self, *args, **kwargs):
        super(ManyToManyField_NoSyncdb, self).__init__(*args, **kwargs)
        self.creates_table = False
 
class User(models.Model):
    groups = ManyToManyField('Group', related_name='groups', db_table=u'USERS_TO_GROUPS')
class Group(models.Model):
    users = ManyToManyField_NoSyncdb(User, related_name='users', db_table=u'USERS_TO_GROUPS')

# ManyToManyField.symmetrical : only on self
class Person(models.Model):
  friends = models.ManyToManyField("self") # I am your friend, then you are my friend.
  friends = models.ManyToManyField("self", symmetrical=False) # the oposite

# ManyToManyField.through : to relate additional data
class Contact(models.Model):
    contacts = models.ManyToManyField('self', through='ContactRelationship', symmetrical=False,)

class ContactRelationship(models.Model):
    types = models.ManyToManyField('RelationshipType',related_name='contact_relationships',blank=True)
    from_contact = models.ForeignKey('Contact', related_name='from_contacts')
    to_contact = models.ForeignKey('Contact', related_name='to_contacts')

    class Meta:
        unique_together = ('from_contact', 'to_contact')

# For simetrical self, add related_name='related_contacts+', to Contact
crm.ContactRelationship.objects.create(from_contact=contact_a, to_contact=contact_b)
crm.ContactRelationship.objects.create(from_contact=contact_b, to_contact=contact_a)

