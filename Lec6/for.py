# for loop
for i in range(2, 6):
    print(i, i*i)

# Display population from 2014 to 2018
pop = 300000
print('{0:10} {1}'.format('Year', 'Population'))
for year in range(2014, 2019):
    print('{0:<10d} {1:,d}'.format(year, round(pop)))
    pop += pop*0.03

# Calculate the balance in savings accounts
initDeposit = eval(input('Enter amount deposit: '))
annualRateOfInterest = eval(input('Enter annual rate of interest: '))
monthlyRateOfInterest = annualRateOfInterest/12
print('\n{0}{1:>12}'.format('Month', 'Balance'))
for i in range(3, 13, 3):
    print('{0:2}        {1:<15,.2f}'.format(
        i, initDeposit*(1+monthlyRateOfInterest)**i))

# Display Multiplication schedule
for i in range(1, 6):
    for j in range(1, 6):
        print('{0} x {1} = {2}'.format(i, j, i*j), end='\t')
    print()

# Display trialngle of asterisks
for i in range(0, 5):
    for j in range(i+1):
        print('*', end='')
    print()
for i in range(5, -1, -1):
    for j in range(i+1):
        print('*', end='')
    print()

# Reverse a letter in a word
word = input('Enter a word to reverse: ')
reversedWord = ''
for letter in word:
    reversedWord = letter+reversedWord
print(reversedWord)

# Display months contains letter 'r'
months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')
for month in months:
    if 'r' in month.lower():
        print(month)

# Replace month with it's 3 - letters
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
for i in range(len(months)):
    months[i] = months[i][0:3]+'.'
print(months)
# Display the name of 52 cards in a deck of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'jack', 'queen', 'king', 'ace']
suits = ['spades', 'hearts', 'clubs', 'diamonds']
deckOfCards = []
for rank in ranks:
    for suit in suits:
        deckOfCards.append(rank + ' of ' + suit)
for card in deckOfCards:
    print(card)

# Display presidents with a specified first name
firstName = input('Enter a first name: ')
flag = False
inFile = open('Files\\forLoop.txt', 'r')
for line in inFile:
    if line.startswith(firstName+''):
        print(line.rstrip())
        flag = True
inFile.close()
if not flag:
    print('President not found!')        

# Display last line in a file
inFile = open('Files\\forLoop.txt','r')
for line in inFile:
    pass
print(line.strip())
inFile.close()

# Add content of file in a list
dataList  = []
inFile = open('Files\\forLoop.txt','r')
for line in inFile:
    dataList.append(line.strip())
inFile.close()    
print(dataList)

# Add content of file in a list
inFile = open('Files\\forLoop.txt','r')
dataList = [line.rstrip() for line in inFile]
inFile.close()
print(dataList)