inFile = open('Files\\namesCount.txt', 'r')
dicOfNames = {}
for line in inFile:
    if line in dicOfNames:
        dicOfNames[line.rstrip('\n')] += 1
    else:
        dicOfNames[line.rstrip('\n')] = 1
print(dicOfNames)
inFile.close()
