# line continuation
print('hello world!, well written code is its own ' +
      'best documentaion.')
quotes = ('hello world!, well written code is its own ' +
          'best documentaion.')
str1 = 'Python'
# out of bound indices string
# print(str1[7])
# print(str1[7])
print(str1[-10:10])
print(str1[-10:3])
print(str1[2:10])
# seperator argument
print('Ali','Fuad','Sami',sep='**')
print('Ali','Fuad','Sami',sep='\t')
print('Ali','Fuad','Sami',sep='\\')
# end argument
print('Ali','Fuad','Sami',end='\t')
print('Ali','Fuad','Sami',end='\\')
print('Ali','Fuad','Sami',end='**')
# escaping characters
print('Muhanned\n')
print('Muhanned\t')
print('\'Muhanned\'')
print('Muhanned\\')
# justify content of string
print(str1.ljust(50))
print(str1.center(50))
print(str1.rjust(50))
print('1'.center(5),'Ahmed'.ljust(20),'100'.rjust(3))
print('2'.center(5),'Fuad'.ljust(20),'200'.rjust(3))
print('3'.center(5),'Omar'.ljust(20),'300'.rjust(3))