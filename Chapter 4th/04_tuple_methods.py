tuple = ("Hello", "World", "I am", "Perry")
num = (1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,76,7,78,87,8,10)
a = num.count(1) #counts how many time 1 has been repeted
print(a)
b = num.index(1) #finds the first index where 1 is availavle, once it finds where its first occurance it will stop searching and return the index in console.
c = num.__contains__(1)
print(c) #if the variable contains the specified text or number. Possible outputs: true or false

print(b)

