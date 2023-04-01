# return multiple values
def name(name):
    n = name.index(' ')
    first = name[:n]
    last = name[n+1:]
    return first, last


first, last = name('Muhanned Alsoradi')
fullName = name('Khalid Mohammed')
print('First name: '+first, 'Last name: '+last, sep='\n')
print('First name: '+fullName[0], 'Last name: '+fullName[1], sep='\n')
# List comprehension
list1 = [ord(x) for x in 'abc']
print(list1)
print([x**.5 for x in (4, -1, 9) if x >= 0])
print([x**2 for x in range(3)])
