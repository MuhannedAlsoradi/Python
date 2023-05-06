# formatting string
print("{0:^5s}{1:<20s}{2:>3s}".format('Ali', 'Ahmed', 'Mohammed'))
print("{0:^5n}{1:<20n}{2:>3n}".format(10, 20, 30))
print("{0:^5n}{1:<20s}{2:>3n}".format(1, 'Muhanned', 5))
print("{0:^5n}{1:<20s}{2:>3n}".format(2, 'Muhanned', 10))
print("{0:^5n}{1:<20s}{2:>3n}".format(3, 'Muhanned', 15))
# formatting numbers
print("{0:10d}".format(12345678))
print("{0:10,d}".format(12345678))
print("{0:10,.2f}".format(1234.5678))
print("{0:10.2f}".format(1234.5678))
print("{0:10,.3f}".format(1234.5678))
print("{0:10.2%}".format(12.345678))
print("{0:10,.3%}".format(12.34569))
# formatting example
print("The area of {0:s} is {1:,d} square miles.".format('Texas', 268820))
str1 = 'The population of {0:s} is {1:.2%} of U.S. population.'
print(str1.format('Texas', 26448000/309000000))
