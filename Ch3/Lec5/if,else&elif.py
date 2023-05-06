# if statement
num1 = eval(input('Enter the first number: '))
num2 = eval(input('Enter the second number: '))
if num1 > num2:
    print('num1 greater than num2')
    largeValue = num1
    print(largeValue)
else:
    print('num2 greater than num1')
    largeValue = num2
    print(largeValue)
answer = eval(input('How old are you: '))
if answer >= 18:
    print('You are Youth person')
else:
    print('you are an teenager')
first = eval(input('First number: '))
sec = eval(input('Second number: '))
third = eval(input('Third number: '))
max = first
if sec > max:
    max = sec
if third > max:
    max = third
print('Max number is {:}'.format(max))
# nested if-else
color = input('Enter a color [Blue or Red]: ').upper()
mode = input('Enter a mode [Steady or Flashing]: ').upper()
result = ''
if color == 'BLUE':
    if mode == 'STEADY':
        result = 'Clear view'
    else:
        result = 'Clouds Due'
else:
    if mode == 'STEADY':
        result = 'Rain Ahead'
    else:
        result = 'Snow Ahead'
print('The result forecast is ', result)
# Evaluate profit
costs = eval(input('Enter total costs: '))
revenue = eval(input('Enter total revenue: '))
result = ''
loss = 0
if costs == revenue:
    result = 'Break even'
else:
    if costs < revenue:
        profit = revenue-costs
        result = 'Profit is ${0:,.2f}.'.format(profit)
    else:
        loss = costs-revenue
        result = 'Loss is ${0:,.2f}.'.format(loss)
print(result)
# elif clause
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')
if num1.isdigit() and num2.isdigit():
    if eval(num1) > eval(num2):
        print('The largest value is', str(num1)+'.')
    elif eval(num1) < eval(num2):
        print('The largest value is', str(num2)+'.')
    else:
        print('The two values is equals.')
else:
    print('Invalid input!')
ytdEarning = eval(input('Enter total earnings: '))
curEarnings = eval(input('Enter the earnings for the current pay period: '))
total = ytdEarning+curEarnings
tax = 0
if total <= 117000:
    tax = 0.062*curEarnings
elif ytdEarning < 117000:
    tax = 0.062*(117000-ytdEarning)
medTax = 0.0145*curEarnings
if ytdEarning > 200000:
    medTax += 0.009*curEarnings
elif total > 200000:
    medTax += 0.009*(total-200000)
ficaTax = tax+medTax
print('FICA Tax for current pay period: ${0:,.2f}'.format(ficaTax))
# gpa grades
gpa = eval(input('Enter your gpa: '))
if gpa >= 3.9:
    print('Excellent!')
elif gpa >= 3.6:
    print('Very good!')
elif gpa >= 3.3:
    print('Good!')
else:
    print('Pass!')
# True & False
if 7:
    print('A nonzero number is true')
else:
    print('Zero number is false')
if []:
    print('An notEmpty list is true')
else:
    print('An empty list is false')
if ['spam']:
    print('An notEmpty list is true')
else:
    print('An empty list is false')
