translate = {'one': 'red', 'two': 'blue', 'three': 'yellow', 'four': 'green'}
for k in translate:
    print(k, translate[k])
bob = {'firstName': 'Muhanned', 'lastName': 'Alsoradi', 'age': 20}
print(bob['firstName'], bob['lastName'], 'is', bob['age'], 'years old.')
print(len(bob), 'age' in bob, ('age', 19) in bob, ('age', 19)not in bob)
bob['age'] = 21
bob['date'] = '9-11-2003'
print(bob)
# print(bob['salary']) # will throwing an exception
print(bob.get('firstName', 'any name'))
print(list(bob.keys()))
print(list(bob.values()))
print(list(bob.items()))
print(list(bob))
print(tuple(bob))
print(set(bob))
del bob['age']
print(bob)
bob = {}
print(bob)
c = dict(bob)
print(c)
c = dict({'a': 97, 'b': 98, 'c': 99})
print(c)
c.clear()
print(c)
bob = {'firstName': 'Muhanned', 'lastName': 'Alsoradi', 'age': 20}
c.update(bob)
print(c)
print(max(c))
print(min(c))
for k in bob:
    print(k, bob[k])
lst = [('one', 1), ('two', 2), ('three', 3)]
d = dict(lst)
print(lst)
print(d)
# # will throwing an exception
# lst = ['one', 'two', 'three']
# d = dict(lst)
# print(lst)
# print(d)
