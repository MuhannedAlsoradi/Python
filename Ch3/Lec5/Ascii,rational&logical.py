# chr(), ord()
print(chr(162))
print(chr(177))
print(chr(97))
print(chr(65))
print(chr(32))
print(ord('A'))
print(ord('a'))
print(ord('¢'))
print(ord('±'))
# Rational operators
print(3 < 3.5)
print([3, 5] < [4, 5])
print([2, 3] != [4, 5, 6])
print(5 in (4, 5, 6))
print('Ahmed' >= 'Omar')
print('Ahmed' not in 'Omar')
print(['Ok', '7', 'Hi'] < ['7', 'two', 'hello!'])
print(1 <= 1)
print(1 < 1)
print('cat' < 'car', 'test')
print('Dog' < 'dog')
print('fun' in 'refund')
a = 4
b = 6
c = 'aaa'
d = 'aaa'
print((a+b) < (2*a))
print((len(c)-b) == (a/2))
print(c < ('good'+d))
# Sorting items in a list
list1 = [5, -10, -6, 12, 20]
list1.sort(reverse=False)
print(list1)
list2 = ['hi', 'ha', 'B', '7']
list2.sort(reverse=True)
print(list2)
list3 = [chr(177), 'cat', 'car', 'Dog', 'dog', '8-balls', '5'+chr(65)]
list3.sort()
print(list3)
list4 = [('B', 5), ('C', 6), ('E', 2), ('F', 3)]
list4.sort()
print(list4)
# Logical operators
n = 4
answ = 'Y'
print((2 < n) and (n < 6))
print((2 < n) or (n == 6))
print(not (n < 5))
print((answ == 'Y') or (answ == 'y'))
print(((answ == 'Y') or (answ == 'y')) or (n < 2))
number = 0
m = 3
print((number != 0) and (m == (n/number)))
# boolean data type
x = 3
y = 2
var = x < y
print(var)
x = 5
print((3+x) < 7)
# startwith(), endswith() & isinstance()
str1 = 'Khalid'
print(str1.startswith('K'))
print(str1.endswith('D'))
print(isinstance(str1, str))
print(type(str1))
print(type(3.8))
print(type(True))
print(type({}))
print(type([]))
print(type((1, 2)))
# Methods return bool value
print(str1.isdigit())
print(str1.isalpha())
print(str1.isalnum())
print(str1.islower())
print(str1.upper().isupper())
print(' '.isspace())
state = 'Gaza'
print(state in ['Rafah', 'KhanYounes', 'Gaza', 'BaitHanoun'])
print(state not in ('Rafah', 'KhanYounes', 'Gaza', 'BaitHanoun'))
print((10 < x <= 30))
print(not (10 < x <= 30))
print((x >= 10) or (x < 30))
