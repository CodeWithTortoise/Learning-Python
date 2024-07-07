# detect double space
a = "a  a"
print(a.find("  "))

# replace double space with single space
print(a.replace("  ", " "))
# strings are immutable which meaans you cant change them by using or executing functions.
print(a)
