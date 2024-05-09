set1={1,2,5,6,7}
print(set1)
print(len(set1))
set2={'apple','orange','lemon',1}
print(set2)
# check an element
print('apple' in set2)
#to add element
set2.add(5)
print(set2)
#to add more than one element
set1.update(['rifa','nida'])
print(set1)
#to remove
set2.remove(5)
print(set2)
set2.discard('apple')
#print(set2)
#set2.remove(10)
print(set2)
set2.discard(12)
print(set2)
#mathematical operations
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
set1.clear()
print(set1)
del set1
print(set1)

