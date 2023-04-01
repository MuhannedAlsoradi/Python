# Functions
def main():
    print(isVowelWord('Ahmed'))
    print(occurringVowels('important'))


def fahrenheitToCelsius(t):
    convertedTemp = (5/9)*(t-32)
    return convertedTemp


def firstName(name):
    n = name.index(' ')
    firstName = name[0:n]
    return firstName


def triple(x):
    x = x*3
    return x


def pay(wage, hours):
    if hours <= 40:
        amount = wage * hours
    else:
        amount = (wage*40)+((1.5)*wage*(hours-40))
    return amount


def futureValue(p, r, m, t):
    i = r/m
    n = m*t
    amount = p*((1+i)**n)
    return amount


def isVowelWord(word):
    word = word.upper()
    vowels = ['A', 'E', 'I', 'O', 'U']
    for ch in vowels:
        if ch in word:
            return True
        else:
            return False


def occurringVowels(word):
    word = word.upper()
    occurredVowels = []
    vowels = ('A', 'E', 'I', 'O', 'U')
    for vowel in vowels:
        if (vowel in word) and (vowel not in occurredVowels):
            occurredVowels.append(vowel)
    return occurredVowels


print(int(3.5))
print(float(3.5))
print(eval('3.5'))
print(chr(65))
print(ord('A'))
print(round(2.34, 1))
print('Your first name:', firstName('Muhanned Alsoradi'))
print('Celsius equivalent: ', fahrenheitToCelsius(212), 'degrees')
num = 3
print(triple(num))
print(num)
print('${0:,.2f}'.format(pay(24.50, 45)))
print('Balance after 5 years: ${0:,.2f}'.format(futureValue(1000, 0.04, 4, 5)))
main()
