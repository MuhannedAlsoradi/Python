team = ['Ali', 12, 'omar']
nums = [5, 10, 4, 5]
words = ['spam', 'hi']
print(nums)
print(team)
print(words)
print(type(team))  # return the type of variable <class 'list'>
print(type(nums))
print(type(words))
print(len(words))  # return the length
print(max(nums))  # return the max value
print(min(nums))  # return the min value
print(sum(nums))  # return the sum
print(nums.count(5))
print(team.index('omar'))
words.reverse()
print(words)
# team.clear()
print(team)
nums.append(7)
print(nums)
words.extend(['Ahmed', 'Khalid'])
print(words)
del team[0]
x = [50, [100, 150]]
print(x)
x.remove(50)
print(x)
x.insert(0, 'ali')
print(x)
print([1, 2]+['ali', 'omar'])
print([0]*6)
# list example
# grades = []
# num = float(input('Enter the 1 grade: '))
# grades.append(num)
# num = float(input('Enter the 2 grade: '))
# grades.append(num)
# num = float(input('Enter the 3 grade: '))
# grades.append(num)
# minGrade = min(grades)
# grades.remove(minGrade)
# avgGrades = sum(grades)/len(grades)
# print('avg grades is {0:.2f} '.format(avgGrades))
# lists slicing
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
print(list1[1:3])
print(list1[-4:-2])
print(list1[:4])
print(list1[4:])
print(list1[:])
del list1[1:3]
print(list1)
print(list1[2:len(list1)])
print((list1[1:3])[1])
print(list1[3:2])
# split method
print('a,b,c'.split(','))
print('a**b**c'.split('**'))
print('a\nb\nc'.split('\n'))
# join method
lines = ['To','be','or','not','to','be']
print(' '.join(lines))
print(' '.join(words))
print(', '.join(words))