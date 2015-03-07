# argv[0] # is the name of the python file


# Lists
l = ['spam','and','eggs']
print ' '.join(l) # spam and eggs
del l[1] # remove list item

# strings
assert 'str' 'ing' == 'str' + 'ing'
x = 'str'.strip() + 'ing'
# x = 'str'.strip()'ing'
# x = 'str'.strip() 'ing'
print x


# 
# # 
# object.__repr__(self) # official string representation of an object (reverse quotes also do that) 
# object.__str__(self) # Called by the str() and by the print statement for `informal` string representation of an object. 
# # it does not have to be a valid Python expression.
# ===================================
# for i in range(10): print "*",
# print i # * * * * 
# ===================================
# >>> 
# ===================================
# resultado = string.replace("gato come gato", "gato", "perro")
# ===================================
# array.array(typecode[, initializer])
# 
# print resultado
# 
import types, exceptions
 
def get_text(o):
	if type(o) is types.FileType: # error type
		text = o.read()
	else:
		raise exceptions.TypeError
	return text
    
try:
	x = int(raw_input("Please enter a number: "))
	break
except ValueError:
	print "Oops!  That was no valid number"
