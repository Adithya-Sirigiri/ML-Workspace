a=5
b=5
print(id(a))
print(id(b))
print(a is b)

#a=5
#b='5'
#print(a is b) it will return false as both are different and have different memory addresses


#a=5
#print(id(a))
#a=7
#print(id(a))
#both will have different ids as python creates 2 different ids for the same variable