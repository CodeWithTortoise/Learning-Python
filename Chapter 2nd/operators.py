print('''There are 4 type of operator
assignment operator
Airthmetic operator
comparision operator
Logical operator
''')

a = 1
b = 2
print(a + b)
print("The remainder is:", a%b)
print("a%b means a is outside and b is inside, hence b is divided by a.")

# = is a assignment operator
# = - / * all are airthmetic operators

c = 1 == 1
print(c)
d = 2 != 5
print(d)
g = 1 > 2
print(g)
h = 2 < 1
print(h)
s = 2 >= 2
print(s)
l = 5 != 5
print(l)
# This is a comparision operator
# comparision operators always gives Boolean values aka true or false

# e = 1
# f += 5
# print(f)

# This gives a error because the intial value of f is not provided to python
# The correct program is as follow


# These are comparision operators
e = 100
e += 800
print(e)

f = 90
f -= 45
print(f)


# logical operators

e = True or False
print(e)
# Truth table of and
print("-------------Truth table of and-----------")
print("True and False is", True and False)
print("True and True is", True and True)
print("False and true is", False and True)
print("False and False is", False and False)
# Truth table of or
print("------------- Truth Table of OR -----------")
print("True or False is", True or False)
print("True or True is", True or True)
print("False or True is", False or True)
print("False or False is", False or False)

# not logical operator
# This will alwaysa give false
print("This will alwaysa give false")

print(not (True))

# This will always give true
print("This will always give true")
print(not (False))


# This was all about operators
