# write a program that asks the user to enter a distanc in kilometers, and then
#cnverts that distance to miles
# 10/1/2018
# CTI-110 P5T1_KilometerConverter 
# Jerome Pinckney
#

# this program converts kilometers to miles
CONVERSION_FACTOR = 0.6214

#the main function gets a distance in kilometes and calls
# the show_miles function to convert it
def main():
    # get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)

# the shoe_miles function converts the parameter km from
# kilometers to miles and displays the result.
def show_miles(km):
    #calculate miles.
    miles = km * CONVERSION_FACTOR

    # display the miles.
    print(km, 'kilometers equal', miles, 'miles.')

# call the main funtion
main()
