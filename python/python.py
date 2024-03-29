# Replace ROAD by RD.
re.sub('ROAD$', 'RD.', s)
s[:-4] + s[-4:].replace('ROAD', 'RD.')


################## Sequence Types ##################
str, unicode, list, tuple, bytearray, buffer, xrange

s + t               # the concatenation of s and t	(6)
s * n, n * sn       # shallow copies of s concatenated	(2)
s[i]	            # i‘th item of s, origin 0	(3)
s[i:j]	            # slice of s from i to j	(3)(4)
s[i:j:k]            # slice of s from i to j with step k
len(s)              # length of s	 
min(s)              # smallest item of s	 
max(s)              # largest item of s	 
s.index(i)          # index of the first occurence of i in s	 
s.count(i)          # total number of occurences of i in s	 

##
## Strings
##
str.capitalize()
str.center(width[, fillchar])
str.count(sub[, start[, end]])
str.decode([encoding[, errors]])
str.encode([encoding[, errors]])
str.endswith(suffix[, start[, end]])
str.expandtabs([tabsize])
str.find(sub[, start[, end]])   # Lowest index in the string where substring sub is found (-1 if not found)
str.index(sub[, start[, end]])  # Like find(), but raise ValueError when the substring is not found.
str.isalnum()
str.isalpha()
str.isdigit() # Return true if all characters in the string are digits and there is at least one character
str.islower()
str.isspace()
str.istitle() # Return true if the string is a titlecased string and there is at least one character
str.isupper()
str.join(iterable)
str.ljust(width[, fillchar])
str.lower()
str.lstrip([chars]) # Return a copy of the string with leading characters removed. defaults: whitespace. 
'www.example.com'.lstrip('cmowz.') # 'example.com'
str.partition(sep)  # Split the string at the first occurrence of sep, and return a 3-tuple
str.replace(old, new[, count])
str.rfind(sub[, start[, end]])
str.rindex(sub[, start[, end]])
str.rjust(width[, fillchar])
str.rpartition(sep) # Split the string at the last occurrence of sep, and return a 3-tuple
str.rsplit([sep[, maxsplit]]) # Return a list of the words in the string, using sep as the delimiter string.
str.rstrip([chars])
'mississippi'.rstrip('ipz') # 'mississ'
str.split([sep[, maxsplit]])
str.splitlines([keepends]) # Return a list of the lines in the string, breaking at line boundaries. 
str.startswith(prefix[, start[, end]]) # Return True if string starts with the prefix
str.strip([chars]) # Return a copy of the string with the leading and trailing characters removed.
'www.example.com'.strip('cmowz.') # 'example'
str.swapcase() # Return a copy of the string with uppercase characters converted to lowercase and vice versa.
str.title()    # Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
str.upper()
str.zfill(width) # Return the numeric string left filled with zeros in a string of length width. 
unicode.isnumeric()
unicode.isdecimal()

# Python has 002 quote types.
print '%(lang)s has %(num)03d quote types.' % {"lang": "Python", "num": 2}

'd'	Signed integer decimal.	 
'i'	Signed integer decimal.	 
'x'	Signed hexadecimal (lowercase).	(2)
'X'	Signed hexadecimal (uppercase).	(2)
'e'	Floating point exponential format (lowercase).	(3)
'E'	Floating point exponential format (uppercase).	(3)
'f'	Floating point decimal format.	(3)
'F'	Floating point decimal format.	(3)
'c'	Single character (accepts integer or single character string).	 
'r'	String (converts any Python object using repr()).	(5)
's'	String (converts any Python object using str()).	(6)
'%'	No argument is converted, results in a '%' character in the result.

"""------------------------------------------------------
    Mutable sequence: Lists
------------------------------------------------------"""
l = [22, True, "una lista", [1, 2]]
l = list('abc')       # returns ['a', 'b', 'c'] 
l = list( (1, 2, 3) ) # returns [1, 2, 3]. 
l = list()            # empty list, []
for i in range(3):
    print i # 0 1 2
  
for index, item in enumerate(items):
    print index, item

for i in range(len(items)):
    print i, items[i]
    
i = iter(L)
item = i.next() # fetch first value
item = i.next() # fetch second value

s[i] = x      # item i of s is replaced by x	 
s[i:j] = t    # slice of s from i to j is replaced by the contents of the iterable t	 
del s[i:j]    # same as s[i:j] = []	 
s[i:j:k] = t  # the elements of s[i:j:k] are replaced by those of t	(1)
del s[i:j:k]  # removes the elements of s[i:j:k] from the list	 
s.append(x)   # same as s[len(s):len(s)] = [x]	(2)
s.pop([i])    # same as x = s[i]; del s[i]; return x	(6)
s.extend(x)   # same as s[len(s):len(s)] = x	(3)
s.count(x)    # return number of i‘s for which s[i] == x	 
s.index(x[, i[, j]])  # return smallest k such that s[k] == x and i <= k < j	(4)
s.insert(i, x)        # same as s[i:i] = [x]	(5)
s.remove(x)   # same as del s[s.index(x)]	(4)
s.reverse()   # reverses the items of s in place	(7)
s.sort([cmp[, key[, reverse]]]) # sort the items of s in place	(7)(8)(9)(10)

"""------------------------------------------------------
    Dictionary
------------------------------------------------------"""
dict1 = {'jack': 4098, 'sjoerd': 4127} or {4098: 'jack', 4127: 'sjoerd'}
dict2 = {"one": 1, "two": 2}
dict(one=1, two=2)
dict({'one': 1, 'two': 2})
dict(zip(('one', 'two'), (1, 2)))
dict([['two', 2], ['one', 1]])

len(d)
d[key]
d[key] = value
del d[key]
key in d     # Return True if d has a key key, else False.
key not in d # Equivalent to not key in d.
iter(d)      # Return an iterator over the keys of the dictionary. iterkeys().
clear()
copy()
has_key(key)     # Deprecated in favor of "key in dict"
items()          # Return a copy of the dictionary’s list of (key, value) pairs.
iteritems()      # Return an iterator over the dictionary’s (key, value) pairs. See the note for dict.items().
iterkeys()       # Return an iterator over the dictionary’s keys. See the note for dict.items().
itervalues()     # Return an iterator over the dictionary’s values. See the note for dict.items().
keys()           # Return a copy of the dictionary’s list of keys. See the note for dict.items().
fromkeys(seq[, value]) # Create a new dictionary with keys from seq and values set to value.
get(key[, default])    # Return the value for key if key is in the dictionary, else default. 
                       # Return None if there is no default get('three', 'no existe key')
pop(key[, default]) # If key is in the dictionary, remove it and return its value, else return default. 
                    # If default is not given and key is not in the dictionary, a KeyError is raised.
popitem()        # Remove and return an arbitrary (key, value) pair from the dictionary.
                 # If the dictionary is empty, calling popitem() raises a KeyError.
setdefault(key[, default])  # If key is in the dictionary, return its value. 
                            # If not, insert key with a value of default and return default.
update([other]) # Update the dictionary with the key/value pairs from other, overwriting existing keys.
values()
viewitems()
viewkeys()
viewvalues()

	      
################## Python Truth ##################
# Any object can be tested for truth value, for use in an if or while 
# condition or as operand of the Boolean operations below.
# The following values are considered false:
	None
	False
	zero of any numeric type, for example, 0, 0L, 0.0, 0j.
	any empty sequence, for example, '', (), [].
	any empty mapping, for example, {}.
	instances of user-defined classes, if the class defines a 
	__nonzero__() or __len__() method, when that method returns 
	the integer zero or bool value False.

################## *args, **kwargs ##################
def test_var_args(farg, *args):
    print "formal arg:", farg
    for arg in args:
        print "another arg:", arg

test_var_args(1, "two", 3)

# formal arg: 1
# another arg: two
# another arg: 3

-----------------------------------------------------
def test_var_kwargs(farg, **kwargs):
    print "formal arg:", farg
    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])

test_var_kwargs(farg=1, myarg2="two", myarg3=3)

# formal arg: 1
# another keyword arg: myarg2: two
# another keyword arg: myarg3: 3

-----------------------------------------------------
def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args = ("two", 3)
test_var_args_call(1, *args)

# arg1: 1
# arg2: two
# arg3: 3

-----------------------------------------------------
def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

kwargs = {"arg3": 3, "arg2": "two"}
test_var_args_call(1, **kwargs)

# arg1: 1
# arg2: two
# arg3: 3

################## read files ##################
f = open("archivo.txt", "w")
completo = f.read(512)
while True:
	linea = f.readline()
	if not linea: break
	print linea

# python comparison
object.__lt__(self, other) # <
object.__le__(self, other) # <=
object.__eq__(self, other) # ==
object.__ne__(self, other) # !=
object.__gt__(self, other) # >
object.__ge__(self, other) # >=
object.__cmp__(self, other)

"""------------------------------------------------------
    Expresions in python
------------------------------------------------------"""
false = False, None, 'numeric zero of all types', 'empty strings/containers'
true = True, 'All other values'

# The operators "is" and "is not" test for object identity: 
x is y:
   return True # If only if x and y are the same object. 

# The operators "in" and "not in" test for collection membership. 
x in s:
	return True # If x is a member of the collection s
