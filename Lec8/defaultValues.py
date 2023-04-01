def total(a, b, c=5, d=10):
    return a+b+c+d


print(total(1, 2))
print(total(1, 2, 3))
print(total(1, 2, 3, 4))


def area(x, y=0):
    if y != 0:
        return x*y
    else:
        return x*x


print(area(10))
print(area(10, 20))
q = 'What is the capital of palestine?'
answer = 'Jerusalem'


def capitalOfPalestine(q, answer, attempts=3):
    noOfAttempts = 0
    while noOfAttempts < attempts:
        noOfAttempts += 1
        ans = input(q)
        if ans == answer:
            print('Correct!')
            break
    if ans != answer:
        print('You have finished all attempts!',
            'The correct answer is: '+str(answer), sep='\n')
capitalOfPalestine(q=q,answer=answer)
capitalOfPalestine(q=q,answer=answer,attempts=1)