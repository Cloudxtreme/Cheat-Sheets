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

