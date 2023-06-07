try:
    num = int(input('Enter a number: '))
    print(num)
except ValueError as ex:
    print('Invalid value!')
except ValueError:
    print('Invalid value!')
except:
    print('Invalid value!')
#
try:
    infile = open('fileeeee.txt', 'r')
    num = float(infile.readline())
except FileNotFoundError:
    print('File not found!')
except ValueError:
    print('Invalid value!')
except TypeError:
    print('Invalid Type!')
except ZeroDivisionError:
    print('Division by zero!')
except:
    print('Error occured!')
