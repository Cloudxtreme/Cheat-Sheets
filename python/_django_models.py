* Creating and saving
{{{
ringo = Person.objects.create(name="Ringo Starr")
p1 = Publisher(name='Addison-Wesley', address='75 Arlington Street')
p1.save()
p1.delete()
}}}
* Getting and filtering
{{{
publisher_list = Publisher.objects.all()
Publisher.objects.filter(name="Apress Publishing")
Publisher.objects.filter(name__contains="press") # icontains, startswith y, endswith y, range, gt, gte, lt, lte
Name.objects.exclude(Q(alias__isnull=True) | Q(alias__exact=''))
Publisher.objects.filter(~Q(value=0)) # Not equal

Publisher.objects.get(name="Addison-Wesley")
Publisher.objects.get(name="Apress Publishing") # exception if many objects
}}}
*Advanced Filtering
{{{
from django.db.models import Q
Entry.objects.filter(headline__contains='Lennon').count()

Entry.objects.filter(id__in=[1, 3, 4])

cheddar_blogs = Blog.objects.filter(name__contains='Cheddar')
entries = Entry.objects.filter(blog__in=cheddar_blogs)

start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2005, 3, 31)
Entry.objects.filter(pub_date__range=(start_date, end_date))
Entry.objects.filter(pub_date__year=2005)
Entry.objects.filter(pub_date__day=3)
}}}
*Order
{{{
Publisher.objects.order_by("name")
Publisher.objects.order_by("-name")
Publisher.objects.order_by("state_provice", "address")

Publisher.objects.filter(country="U.S.A.").order_by("-name")
}}}
*Limit
{{{
Publisher.objects.all()[0]  #LIMIT 1
Entry.objects.all()[:5] #LIMIT5
Entry.objects.all()[5:10]
Entry.objects.all()[:10:2] #Every second object of the first 10:
Entry.objects.order_by('headline')[0] #The same as the next query
Entry.objects.order_by('headline')[0:1].get()
}}}
*Delete Update
{{{
publishers = Publisher.objects.all()
publishers.delete()
publishers.update(status='inactive')
}}}
*Filters can reference fields on the mode
{{{
from django.db.models import F
Entry.objects.filter(n_comments__gt=F('n_pingbacks'))
Entry.objects.filter(n_comments__gt=F('n_pingbacks') * 2)
Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))
Entry.objects.filter(authors__name=F('blog__name')) # the author's name is the same as the blog name
Proxy.objects.all().update(value= not F('value')) # invert the value
}}}
*Q Object
{{{
Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)
Poll.objects.get(
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
    question__startswith='Who'
)
}}}
*Count(field, distinct=False), Avg(field), Max(field), Min(field), Sum(field), StdDev(field, sample=False)
{{{
q = Blog.objects.annotate(Count('entry')) # how many entries have been made in each blog
q[0].name # The name of the first blog
q[0].entry__count # The number of entries on the first blog

q = Blog.objects.annotate(number_of_entries=Count('entry'))
q[0].number_of_entries
}}}
*We need {{{select category_id, count(id) from item group by category_id}}}
{{{
class Category(models.Model):
    name = models.CharField(max_length=60)

class Item(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category)
}}}
We can do this:
{{{
from django.db.models import Count
theanswer = Item.objects.values('category').annotate(Count('category')).order_by()
}}}
