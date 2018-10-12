# write a program that keeps a
# running total of the number of bugs collected during the seven days
# 9/25/2018
# CTI-110 P4T2 - Bug Collector
# Jerome Pinckney
#

#Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 8):
    # prompt the user
    print('Enter the bugs collected on day', day)

    # Input the number bufs.
    bugs = int(input())

    # Add bugs to total
    total += bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')
