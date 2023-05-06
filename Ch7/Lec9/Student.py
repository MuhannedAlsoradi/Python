def main():
    name = input('Enter student name: ')
    midterm = eval(input('Enter student grade on midterm: '))
    final = eval(input('Enter student grade on final: '))
    s1 = Student(name=name, midterm=midterm, final=final)
    print(s1)


class Student:
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

    def __str__(self) -> str:
        return (self.name+'\t'+self.calculateSemGrades())


main()
