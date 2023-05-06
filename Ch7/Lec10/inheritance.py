class Student(object):
    def __init__(self, name='', midterm=0, final=0):
        self.name = name
        self.midterm = midterm
        self.final = final

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMidTerm(self, midterm):
        self.midterm = midterm

    def getMidTerm(self):
        return self.midterm

    def setFinal(self, final):
        self.final = final

    def getFinal(self):
        return self.final

    def __str__(self) -> str:
        return (self.name+'\t'+self.calculateSemGrades())


class Person():
    def __init__(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age


class MsStudent(Student):
    def calculateSemGrades(self):
        avg = round((self.midterm+self.final)/2)
        if avg >= 90:
            return 'E'
        elif avg >= 80:
            return 'V.G'
        elif avg >= 70:
            return 'G'
        elif avg >= 60:
            return 'P'
        else:
            return 'F'


class PStudent(Student, Person):
    def __init__(self, age=0, name='', midterm=0, final=0, fullTime=True):
        self.fullTime = fullTime
        Person.__init__(self, age=age)
        Student.__init__(self, name=name, midterm=midterm, final=final)

    def calculateSemGrades(self):
        avg = round((self.midterm+self.final)/2)
        if avg >= 60:
            return 'Pass'
        else:
            return 'Fail'

    def __str__(self):
        if self.fullTime:
            status = '\tFull-time student'
        else:
            status = '\tPart-time student'
        return super().__str__()+status


s1 = MsStudent(name='Ali', midterm=89, final=90)
print(s1)
print(s1.calculateSemGrades())
s2 = PStudent(name='Dina', midterm=76, final=80, age=20)
print(f'{s2}')
print(f'{s2.getName()} is {s2.getAge()} years old.')
print(s2.calculateSemGrades())
s3 = PStudent(name='Dina', midterm=76, final=80, age=20, fullTime=False)
print(s3)
lst = [s1, s2, s3]
