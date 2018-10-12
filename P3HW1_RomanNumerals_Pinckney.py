# CTI-110 
# P3HW1 - Roman Numerals 
# Jerome Pinckney
# 9/17/2018
#program Pseudocode ( detail algorithm)

print('Enter number between 1 and 10')

#enter a nummber 1-10
number = int(input('number: '))

#convert number to roman numeral
if number == 1:
    print('I')
elif number == 2:
    print('II')
elif number == 3:
    print('III')
elif number == 4:
    print('IV')
elif number == 5:
    print('V')
elif number == 6:
    print('VI')
elif number == 7:
    print('VII')
elif number == 8:
    print('VIII')
elif number == 9:
    print('IX')
elif number == 10:
    print('X')
else:
    print('ERROR not a number between 1-10')
