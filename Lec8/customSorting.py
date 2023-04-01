def main():
    list1 = ['aaaa a', 'a aa', 'a pk', 'aai d']
    list1.sort(key=len)
    print(list1)
    list1.sort(key=lambda x: x[-1])
    print(list1)
    list1.sort(key=numOfVowels, reverse=True)
    print(list1)
    list1.sort(key=lambda name: name.split(sep=' ')[-1])
    print(list1)


def numOfVowels(word):
    vowels = ['a', 'i', 'u', 'e', 'o']
    count = 0
    for i in vowels:
        for chr in word:
            if i == chr:
                count = count + 1
    return count


print(numOfVowels('aaa'))
main()
list1 = ['a', 'c', 'b']
print(list1)
list2 = sorted(list1)
print(list2)
print(list1)
list2 = sorted('spam')
print(list2)
