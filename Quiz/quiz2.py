# Q.1
i = 1
while True:
    if i % 007 == 0:
        break
    print(i, end=' ')
# Q.2
z = 'xyz'
j = 'j'
while j in z:
    print(j)
# Q.3
lst = [i//i for i in range(0, 4)]
sum = 0
for n in lst:
    sum += n
print(sum)
# Q.4
ex = 'helloworld'
print(ex[::-1].startswith('d'))
# Q.5
x = 'abcd'
for i in range(len(x)):
    i.upper()
print(x)
# Q.6
x = 'pqrs'
for i in range(len(x)):
    x[i].upper()
print(x)
# Q.7
for i in [1, 2, 3, 4][::-1]:
    print(i)
