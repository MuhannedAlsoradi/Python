# Q.66
i = int(input('How many numbers do you want to enter? '))
lst = []
for p in range(i):
    num = int(input('Enter a number: '))
    lst.append(num)
if i % 2 == 1:
    median = lst[len(lst)//2]
else:
    median = (lst[len(lst)//2]+lst[(len(lst)//2)-1])/2
print(f'Median: {median}')
# Q.71
grades = []
gradesAbove = []
finalFile = open('Files\\Final.txt', 'r')
for p in finalFile:
    grades.append(eval(p))
finalFile.close()
finalFile = open('Files\\Final.txt', 'r')
avg = sum(grades)/len(grades)
for q in finalFile:
    if eval(q) > avg:
        gradesAbove.append(eval(q))
print(f'Number of grades: {len(grades)}')
print(f'Average grade: {avg}')
print(
    f'Percentage of grades above average: {len(gradesAbove)/len(grades)*100}%')
finalFile.close()
# Q.72
lst = []
for m in range(5):
    num = eval(input('Enter one of five grades: '))
    lst.append(num)
lst.sort()
lst = lst[2:]
print(f'Average grade: {sum(lst)/len(lst):.2f}')
# Q.73
word = input('Enter a word: ')
vowels = ['a', 'e', 'u', 'i', 'o']
targetVowels = []
for chr in word:
    if (chr in vowels) and (chr not in targetVowels):
        targetVowels.append(chr)
print(f'Number of different vowels: {len(targetVowels)}')
