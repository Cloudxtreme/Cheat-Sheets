 sudo apt-get install libxslt-dev
 
#################################################
##                 GAE Model                   ##
#################################################
import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Employee(db.Model):
  name = db.StringProperty(required=True)
  role = db.StringProperty(required=True, choices=set(["executive", "manager", "producer"]))
  date = db.DateProperty()
  completed = db.BooleanProperty()
  account = db.UserProperty()

e = Employee(name="",
             role="manager",
             account=users.get_current_user())
e.hire_date = datetime.datetime.now()
e.put()

# other example, consulta SQL
training_registration_list = [users.User("Alfred.Smith@example.com"),
                              users.User("jharrison@example.com"),
                              users.User("budnelson@example.com")]
employees_trained = db.GqlQuery("SELECT * FROM Employee WHERE account IN :1",
                                training_registration_list)
for e in employees_trained:
    e.new_hire_training_completed = True
    db.put(e)

# poliformismo
from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Contact(polymodel.PolyModel):
  phone_number = db.PhoneNumberProperty()
  address = db.PostalAddressProperty()

class Person(Contact):
  first_name = db.StringProperty()
  last_name = db.StringProperty()
  mobile_number = db.PhoneNumberProperty()

class Company(Contact):
  name = db.StringProperty()
  fax_number = db.PhoneNumberProperty()

######### query example #########
class Story(db.Model):
  title = db.StringProperty()
  date = db.DateTimeProperty()

query = Story.all()
query.filter('title =', 'Foo')
query.order('-date')
query.ancestor(key)
query.filter('title =', 'Foo').order('-date').ancestor(key)

results = query.fetch(10)
for result in results:
  print "title: " + result.title

for result in query:
  print "Title: " + result.title

####################################

### GQL
# Parameters can be bound with positional arguments.
query = db.GqlQuery("SELECT * FROM Story WHERE title = :1 "
                    "AND ANCESTOR IS :2 "
                    "ORDER BY date DESC",
                    'Foo', key)

# Or, parameters can be bound with keyword arguments.
query = db.GqlQuery("SELECT * FROM Story WHERE title = :title "
                    "AND ANCESTOR IS :parent "
                    "ORDER BY date DESC",
                    title='Foo', parent=key)

# String, number and Boolean values can be literal values in the string.
query = db.GqlQuery("SELECT * FROM Story WHERE title = 'Foo' "
                    "AND ANCESTOR IS :parent "
                    "ORDER BY date DESC",
                    parent=key)

results = query.fetch(10)
for result in results:
  print "Title: " + result.title
                  
## ELIMINAR UNA ENTIDADs  
  q = db.GqlQuery("SELECT * FROM Message WHERE create_date < :1", earliest_date)
results = q.fetch(10)
for result in results:
  result.delete()

# or...

q = db.GqlQuery("SELECT * FROM Message WHERE create_date < :1", earliest_date)
results = q.fetch(10)
db.delete(results)

### reference
class Author(db.Model):
  name = db.StringProperty()

class Story(db.Model):
  author = db.ReferenceProperty(Author)

story = db.get(story_key)
author_name = story.author.name


