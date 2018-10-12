# create a table that shows a table of celcius temperatures 0 - 20 and farenheit
# equivelents
# 9/25/2018
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Jerome Pinckney
#

print('celcius to farenheit table')

#setting temperatures c = celcius, f = farenheit
c = -1

print('celcius  farenheit')

# creating rows and columns
for row in range(21):
    for col in range(1):
        c = c + 1
        f = (c * 1.8) + 32
        print(c, end='        ')
        print(f)

