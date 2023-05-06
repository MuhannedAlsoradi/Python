def main():
    x = 2
    print(str(x)+': function main')
    trivial()
    print(str(x)+': function main')


def trivial():
    x = 3
    print(str(x)+': function trivial')


main()

x = 0


def main02():
    print(str(x)+': function main')
    trivial02()
    print(str(x)+': function main')


def trivial02():
    global x
    x += 7
    print(str(x)+': function trivial')


main02()

x1 = 5


def test():
    global x1
    print(str(x1)+': function test')
    x1 = x1+2
    print(str(x1)+': function test')


def test01():
    x = 3
    # global x


test()
print(str(x1)+': x1 value')
CONST_VAR = 3
print(CONST_VAR)