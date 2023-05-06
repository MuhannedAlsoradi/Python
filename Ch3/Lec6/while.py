# while loop
num = 1
while num <= 5:
    print(num)
    num += 1
# input validation
response = '0'
responses = ('3', '1', '2')
while response not in responses:
    response = input('Enter 1, 2 or 3: ')
    if response == '1':
        print('Plastics.')
    elif response == '2':
        print('Rosebud.')
    elif response == '3':
        print('That\'s all folks.')
# find min, max and avg
count = 0
total = 0
print('Enter -1 to terminate entering numbers.')
num = input('Enter a non negative number: ')
if num.isdigit():
    num = eval(num)
    min1 = num
    max1 = num
while num != -1:
    count += 1
    total += num
    if min1 > num:
        min1 = num
    if max1 < num:
        max1 = num
    num = eval(input('Enter a non negative number: '))
if count > 0:
    print('The min value: ', min1)
    print('The max value: ', max1)
    print('The avg value: ', total/count)
# another case to find min, max and avg
list1 = []
print('Enter -1 to terminate entering numbers.')
num = eval(input('Enter a non negative number: '))
while num != -1:
    list1.append(num)
    num = eval(input('Enter a non negative number: '))
if len(list1) > 0:
    list1.sort()
    print('The min value: ', list1[0])
    print('The max value: ', list1[-1])
    print('The avg value: ', sum(list1)/len(list1))
# when i get $1M
numberOfYears = 0
balance = eval(input('Enter init deposite: '))
while balance < 1000000:
    balance += balance*0.04
    numberOfYears += 1
print('In', numberOfYears, 'years you will have a million dollars.')
# break statement
list1 = []
while True:
    num = eval(input('Enter a non negative number: '))
    if num == -1:
        break
list1.append(num)
# continue statement
list1 = ['one', 2, 'two', 17.5, 33, 22.1, 242, 'three']
i = 0
findFlag = False
while i<len(list1):
    x=list1[i]
    i+=1
    if not isinstance(x,int):
        continue
    if x%11==0:
        findFlag=True
        print(x,'is the first int that is divisible by 11.')
        break
if not findFlag:
    print('There is no int number in the list that is divisible by 11.')
# creating a menu
print('Enter a number from the menu to select a model: ')
print('1. text-davince-003')
print('2. gpt-3.5 turbo')
print('3. GPT-4')
print('4. Quit\n')
while True:
    num = int(input('Enter a number: '))
    if num == 1:
        print('1. text-davince-003')
    elif num == 2:
        print('2. gpt-3.5 turbo')
    elif num == 3:
        print('3. GPT-4')
    elif num == 4:
        break
# infinite loop
print('Enter -1 to terminate')
number = 0
while number >= 0:
    number = eval(input('Enter number to square: '))
    number = number*number
    print(number)
