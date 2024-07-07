a = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "asb das kefaslp;p fljqweoq"
print("Lenth of a is:", len(a))
print("Does a ends with z?", a.endswith("z"))
print("Replacing xyz with abc in a:", a.replace("xyz", "abc"))
print("If I captialize a it will look like this:", a.capitalize())
print("If I uppercase a it will look like this:", a.upper())
print("If I lowercase the above uppercase text ut will be:", a.lower())
print("If I want to use b as a title:", b.title())
print("Where is l in the string a?:", a.find("l"))
# chain
print(a.replace("abc", "123".replace("123", "789")))
# if find cant find it returns -1