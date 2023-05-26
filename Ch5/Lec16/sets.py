set1 = {1, 2, 3, 4, 5, 6}
set1.add(1)
print(set1)
set1.discard(1)
print(set1)
set1.clear()
print(set1)
print(set([1, 2, 3, 4, 5]))
print(set((1, 2, 3, 4, 5)))
terms = ['nudge', 'nudge', 'wink', 'wink']
words = set(terms)
print(words)
words = list(words)
print(words)
set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2))
print(set1.union(set2))
print(set2.difference(set1))
set3 = {x**2 for x in range(-3, 3)}
print(set3)
