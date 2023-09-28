data = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}

list = [(key,value) for key, value in data.items()]

print(list)

union1 = set1.union(set2)
print(union1)
union2 = set1 | set2
print(union2)

symmetric1 = set1.symmetric_difference(set2)
print(symmetric1)
symmetric2 = set1 ^ set2
print(symmetric2)

difference1 = set1.difference(set2)
print(difference1)
difference2 = set2.difference(set1)
print(difference2)
difference3 = set1 - set2
difference4 = set2 - set1
print(difference3)
print(difference4)

disjoint1 = set1.isdisjoint(set2)
print(disjoint1)
disjoint2 = set1 & set2
print(disjoint2)

