str1 = 'muhaNneud alSoradi  '
# length of string
print(len(str1))
# to upper case
print(str1.upper())
# to lower case
print(str1.lower())
# capitalize the first character
print(str1.capitalize())
# find the first character from left and return index
print(str1.find('u'))
# find the first character from right and return index
print(str1.rfind('u'))
# capitalize the first char from all words
print(str1.title())
# remove right spaces at the last
print(str1.rstrip('u'))
priase = 'Good mornings'
# chained methods
numOfGees = priase.upper().count('G')
print(numOfGees)

