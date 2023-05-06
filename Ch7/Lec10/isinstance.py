import inheritance
print(isinstance('hello', str))
print(isinstance(1.1, int))
print(isinstance(1.7, float))
print(isinstance([], list))
print(isinstance([1, 2, 3], list))
print(isinstance((), tuple))
print(isinstance((1, 2, 3), tuple))
print(isinstance({'1': 'Hello', '2': 'hi', '3': 'How are you!'}, dict))
print(isinstance({}, dict))
print(isinstance({1, 2, 3}, set))
print(isinstance({}, set))
print(isinstance(set(), set))
psCount = 0
msCount = 0
for s in inheritance.lst:
    if isinstance(s, inheritance.MsStudent):
        msCount += 1
    elif isinstance(s, inheritance.PStudent):
        psCount += 1
print(f'no. of MsStudents {msCount}')
print(f'no. of PStudents {psCount}')
print(isinstance(inheritance.s2, inheritance.Student),
      isinstance(inheritance.s2, inheritance.Person), isinstance(inheritance.s2, inheritance.PStudent))
