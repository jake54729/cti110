# write a function named feet_to_inches that acceptes a numbero feet
# as an arguement an dreturns the number of inches in that many feet
# 8/1/2018
# CTI-110 P5T2_FeetToInches 
# jerome pinckney
#

# consttant fo r the number of inches per foot.
INCHES_PER_FOOT = 12

# main function
def main():
    #get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    #convert that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches')

# the feet_to_inches function coverts feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

#call the main function
main()
