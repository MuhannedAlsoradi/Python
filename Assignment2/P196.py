# Q.59
import math


def largest_prime_factor(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n


numbers = [1208, 290, 1243, 1169, 865]
numbers.sort(key=lambda x: largest_prime_factor(x))
print(f'Sorted by largest prime factor:\n{numbers}\n')
# Q.60
strings = ['Ahmed', 'Salem', 'Omar', 'Dina', 'Othman']
numbers.sort(key=lambda x: str(x)[-1], reverse=True)
print(f'Sorted by last digit:\n{numbers}\n')
