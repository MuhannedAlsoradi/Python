# Q.25
lst = [10, 12, 13, 5, 6, 7, 20, 100, 200, 33]
maximum = lst[0]


def max_value():
    global maximum
    for p in lst:
        if p > maximum:
            maximum = p
    return maximum


print(max_value())


# Q.26


def count_value(str, sub_str):
    count = 0
    begin = 0
    while True:
        begin = str.find(sub_str, begin)
        if begin == -1:
            break
        else:
            count += 1
            begin += len(sub_str)
    return count


print(count_value(str='aaaabbaaaabbaaaabb', sub_str='aa'))


# Q.28


def fact(n):
    if n >= 0:
        if n == 0 or n == 1:
            return n
        return n*fact(n-1)


def getN():
    n = eval(input('Enter a positive integer: '))
    result = fact(n=n)
    print(f'{n}! is {result}')


getN()
