# Q.53
amount = eval(input('Enter amount of tip: '))
percentage = eval(input('Enter percentage tip: '))/100
result = amount*percentage
print('Tip: $'+str(round(result, 2)))
# Q.54
revenue = eval(input('Enter revenue: '))
expenses = eval(input('Enter expenses: '))
income = revenue-expenses
print('Net income ${0:10,.2f}'.format(income))
# Q.55
salary = eval(input('Enter your salary: '))
newSalary = salary + (eval(
    input("Enter The persent of the" +
          " pay raise of the salary : "))/100)*salary
print("The new salary is : {:,.2f}".format(newSalary))
cutSalary = newSalary - (eval(
    input('Enter The persent of the' +
          ' pay cut of the salary : '))/100)*newSalary
change = (cutSalary-salary)/salary
print("The new salary: ${:,.2f} \n  Change of the two new saraly is : {:.2%} ".format(
    cutSalary, change))
