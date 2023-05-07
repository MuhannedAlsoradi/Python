for i in range(5):
    print(i)
x = 1


def a(x):
    return x*2


x = 2+a(x)
print(a(x))
dog = 'Zoomie'
pattern = ''
for letter in dog:
    inPattern = False
    if dog.count(letter) > 1:
        pattern += letter
        inPattern = True
    if dog.count(letter) > 0 and inPattern == False:
        pattern += letter
    else:
        pattern += '.'
print(pattern)


def doSomething(L):
    m = L[0]
    idx = 0
    i = 0
    for x in L:
        if x < m:
            m = x
            idx = i
        else:
            pass
        i += 1
    return m, idx


print(doSomething([1, 2, 3, -5, 7, 9]))
print('{:.3f} {:.3f}'.format(2.5679, 9.0))


class Vechil:
    def __init__(self, name, speed, mileage) -> None:
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return 'The {} seating capacity is {}'.format(self.name, capacity)


class Bus(Vechil):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


bus = Bus('School A', 100, 12)
print(bus.seating_capacity(capacity=50))
lst1 = [0, 2, 5, 1]
str1 = '7'
for l in lst1:
    str1 = str1 + l


class A:
    def __init__(self, x=1):
        self.x = x


class der(A):
    def __init__(self, y=2):
        super().__init__()
        self.y = y


def main():
    obj = der()
    print(obj.x, obj.y)


main()


class test:
    def __init__(self, a):
        self.a = a

    def display(self):
        print(self.a)


obj = test()
obj.display()


d1 = {"abc": 5, "def": 6, "ghi": 7}
print(d1[0])


class A():
    def __init__(self, count=100):
        self.count = count


obj1 = A()
obj2 = A(102)
print(obj1.count)
print(obj2.count)


class Book:
    def __init__(self, author):
        self.author = author


book1 = Book("V.M.Shah")
book2 = book1
print(book1.author)
print(book2.author)
print(id(book1))
print(id(book2))


class A:
    def __init__(self):
        self.count = 5
        self.count = count+1


a = A()
print(a.count)


def rareLetterCheck(testStr):
    rareLetters = ['j', 'k', 'q', 'x', 'z']
    for letter in testStr:
        if letter in rareLetters:
            return letter


s = 'Quick brown fox'
print(rareLetterCheck(s))


def h(L):
    L[1] = [7, 8]
    L[0] = [5, 6]
    L[0][0] = 9
    print(L)


L = [[1, 2], [3, 4]]
h(L)
print(L)
L = [13, 12, 21, 16, 35, 7, 4]
s = 5
s1 = 3
for i in L:
    if (i % 4 == 0):
        s = s + i
        continue
    if (i % 7 == 0):
        s1 = s1 + i
print(s, end=" ")
print(s1)


def reps(aStr, subStrs, times):
    frequent = []
    for subStr in subStrs:
        if aStr.count(subStr) >= times:
            frequent.append(subStr)
    return frequent


text = 'Make that cat go away! Tell that Cat in the Hat you do NOT want to play.'
patterns = ['that', 'cat', 'ay']
print(reps(text, patterns, 2))


class Father():
    def print(self):
        print("Father Enjoys Driving")


class Mother():
    def print(self):
        print("Mother Enjoys Cooking")


class Child(Father, Mother):
    def print(self):
        pass


c = Child()
c.print()
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)
