# write a Boolean function named is_prime which takes an iteger as an argument
#and retura true is the functiion is a prime number, or false oherwise
# 8/1/2018
# CTI-110 P5HW1 - Prime Numbers
# jerome pinckney
#



# determine if prime
def isPrime( userNumber ):
    evenDivisions = 0
    # if any number is less than or equal to 1 it is not prime
    if userNumber <= 1:
        return False
    # make range to divide he current number
    for currentNumber in range( 1, userNumber + 1 ):
        if userNumber % currentNumber == 0:
            evenDivisions = evenDivisions + 1
            if evenDivisions > 2:
                return False
    return True

#main function
def main():
    #get a number from the user
    userNumber = int(input(' Enter a number: '))
    print()
    # if its prime it will say it "is a prime number"
    # if it is not prime it will say "is not a prime number"
    if isPrime( userNumber ):
        print(userNumber, 'is a prime number')
    else:
        print(userNumber, 'is not a prime number')

#call main function
main()
