# Q.33
weight = eval(input('Enter weight in pounds: '))
dollars = eval(input('Enter payment in dollars: '))
print('Your change is ${:.2f}'.format((20)-weight*2.5))
# Q.34
balance = eval(input('Enter current balance: '))
withdrawal = eval(input('Enter amount of withdrawal: '))
if withdrawal > balance:
    print('Withdrawal denied')
elif balance <= 150:
    print('Balance below $150')
else:
    balance -= withdrawal
    print('The new balance is ${:,.1f}'.format(balance))
# Q.35
letter = input('Enter a single uppercase letter: ')
if len(letter) != 1 or letter.islower():
    print('You didn\'t comply with the request.')
# Q.36
year = eval(input('Enter a year: '))
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')
# Q.42
firstSuit = eval(input('Enter the cost of first suit: '))
secondSuit = eval(input('Enter the cost of first suit: '))
# Q.43
income = eval(input('Enter your taxable income: '))
if income <= 20000:
    tax = income*0.2
elif income <= 50000:
    tax = 400+0.25*(income-20000)
else:
    tax = 1150+0.035*(income-50000)
print(f'your tax is ${tax}')
