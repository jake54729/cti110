# write a program that asks the use to enter the amount that he or she has
# budgeted for a month.
# 9/25/2018
# CTI-110 P4HW1 - Budget Analysis
# Jerome Pinckney
#

# Set the accumulator
total = 0               

# Get the budgeted amount
budget = float(input('Budgeted amount for the month: $'))

# Get the expenses
# exp = expenses
exp = int(input('How many expenses do you have? '))

# tell them to enter the expenses
print('Enter the expense amounts.')

# get expense amounts
for Expense in range(exp):
    print('Expense', Expense + 1, end='')
    amt = int(input(': '))
    total += amt

    # get difference between the budget and total
    expense = budget - total
if expense > 0:
    print('You are under budget.')
else:
    print('You are over budget.')
