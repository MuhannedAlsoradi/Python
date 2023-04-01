# Q.31
balance = 1000
print('Options:\n1. Make a Deposit\n2. Make a Withdrawal' +
      '\n3. Obtain Balance\n4. Quit')
while True:
    select = input('Make a selection from the options menu: ').strip()
    if select == '1':
        deposit = eval(input('Enter amount of deposit: '))
        balance += deposit
        print('Deposit processed.')
    elif select == '2':
        while True:
            withdrawal = eval(input('Enter amount of withdrawal: '))
            if withdrawal > balance:
                print('Denied. Maximum withdrawal is $1,500.00')
            else:
                balance -= withdrawal
                print('Withdrawal Processed.')
                break
    elif select == '3':
        print(f'Balance: ${balance}')
    elif select == '4':
        break
