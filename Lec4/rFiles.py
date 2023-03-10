# Create file object
rFile = open('Files\\file.txt', 'r')
# Reading Data
x = rFile.read(10)
str1 = rFile.readline()
str2 = rFile.readlines()
print('1\n'+x)
print('2\n'+repr(str1))
print(str2)
# Close the file
rFile.close()
