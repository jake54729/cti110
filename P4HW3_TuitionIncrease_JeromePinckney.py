# write a program with a loop that displays the projected semester tuition
# for the next 5 years
# 9/25/2018
# CTI-110 P4HW3 - Tuition Increase
# Jerome Pinckney
#

# state tuition and year
tuition = 8000
year = int(-1)

# loop calculation for tuition and year
print('year     tuition')
for year in range(6):    
    print(year , end='    =   ')
    print(format(tuition,'.1f'))
    year = year + 1
    tuition = tuition *1.03
