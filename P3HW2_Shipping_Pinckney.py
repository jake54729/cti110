# CTI-110 
# P3HW2 - Shipping Charges 
# Jerome Pinckney
# 9/17/2018
#program Pseudocode ( detail algorithm)

#get the weight of package
weight = float(input('weight of package(in pounds): '))

#filter weights
if weight <= 2:
    print('Shipping charge is $1.50')
elif weight > 2 and weight <= 6:
    print('Shipping charge is $3.00')
elif weight > 6 and weight <= 10:
    print('Shipping charge is $4.00')
else:
    print('Shipping charge is $4.75')
