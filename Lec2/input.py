twon = input('Enter your city name:')
print(twon)
fullName = input('Enter a full name: ')
n = fullName.rfind(' ')
firstName = fullName[:n]
lastName = fullName[n+1:]
print('first name: '+firstName, 'last name: '+lastName, sep='\n')
