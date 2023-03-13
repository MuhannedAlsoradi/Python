# Q.101
sentence = input('Enter a sentence: ')
list1 = sentence.split(' ')
print('Number of words: {0:}'
      .format(len(list1)))
# Q.102
sentence = input('Enter a sentence: ')
print('First word: {0:s}'
      .format(sentence.split(' ')[0]))
n = (sentence.split(' ')[-1]).index('.')
print('Last word: {0:s}'
      .format((sentence.split(' ')[-1])[:n]))
# Q.103
sentence = input('Enter a 2-part name: ')
print('Revised form: {0:s}, {1:s}'.format(
    sentence.split(' ')[-1].capitalize(), sentence.split(' ')[0].capitalize()))
# Q.104
sentence = input('Enter a 3-part name: ')
print('Middle name: {0:s}'.format(
    sentence.split(' ')[1].capitalize()))