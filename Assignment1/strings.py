# Q.97
numOfSeconds = input('Enter the number of seconds' +
                    ' between lighting and thunder: ')
distance = eval(numOfSeconds)/5
print('Distance from storm: ' + str(distance))
# Q.98
age = input('Enter your age: ')
heartRate = input('Enter your resting heart Rate: ')
trainingHeartRate = 0.7*(220-eval(age))+0.3*eval(heartRate)
print('Training heart Rate: '+str(int(trainingHeartRate))+' beats/min')
# Q.101
nameOfTeam = input('Enter name of team: ')
won = eval(input('Enter number of games won: '))
fail = eval(input('Enter number of games fail: '))
totalPercent = won/(won+fail)
print(nameOfTeam+' won '
    +str('{:.2%}'.format(totalPercent))+' of their games')
# Q.108
purchasePrice = eval(input('Enter purchase price: '))
sellPrice = eval(input('Enter selling price: '))
markup = sellPrice - purchasePrice
if purchasePrice*2 == markup:
    percentageMarkup = 200
else:
    percentageMarkup = markup/purchasePrice * 100
profitMargin = markup/sellPrice *100
print('Markup: $'+str(markup))
print('percentage markup: %'+str(round(percentageMarkup,2)))
print('profit margin: %'+str(round(profitMargin,2)))
# Q.109
number = input('Enter the number: ').strip()
n = number.find('.')
numOfLeft = len(number[:n])
numOfRight = len(number[n+1:])
print(str(numOfLeft)+' digits on the left of decimal point')
print(str(numOfRight)+' digits on the right of decimal point')
# Q.110
sentence = input('Enter a sentence: ')
word = input('Enter word to replace: ')
anotherWord = input('Enter replacement word: ')
list1 = sentence.split(' ')
indexWord = list1.index(word)
list1.insert(indexWord, anotherWord)
list1.remove(word)
sentence = ' '.join(list1)
print(sentence)
# Q.111
months = eval(input('Enter the number of months: '))
print(str(months)+' months is ' + str(months//12)+
    ' years and '+str((months % 12))+' months')
