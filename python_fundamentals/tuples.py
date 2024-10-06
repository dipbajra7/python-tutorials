# tuples are like list but immutable (cannot be modified or changed)
numbers = (1,2,3,4,5)

print(numbers.count(1))
print(numbers.index(2))
print(numbers.__len__())

#unpacking = assigning individual values to a variable.. can be done with lists too
a,b,c,d,e = numbers
print(e)
print(e * d)
