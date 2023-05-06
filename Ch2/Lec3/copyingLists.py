l1 = ['a', 'b']
l2 = l1
l2[1] = 'c'
print(l1, l2)
l2 = list(l1)
l2.insert(3, 'd')
print(l1, l2)
l1 = [1, 2, 3]
l2 = l1[1:]
print(l1, l2)
# print(l1[10])
# print(l1[-10])
l1 = [1, 2, 3, 4, 5, 6]
print(l1[-10:10])
print(l1[-10:3])
print(l1[3:10])
