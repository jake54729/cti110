# Complete the programming challenge exercise #11 Male Female Percentage on page 78.
# 9/10-2018
# CTI-110 P2HW2 - Male Female Percentage
# Jerome Pinckney
#

#get number of males and number of females: M= male, F= female
M= print(input('Number of males: '))
F= print(input(' Number of Females: '))

#calculate Total
Total= F+M


# calculate female and male percentage x100:
# MP= male percentage, FP= female percentage
# MT= male total, FT= female toatal
MP= M// Total
MT= MP* 100

FP= F// Total
FT= FP* 100

#display percentages
print( 'Percentage of Males is: ', MT), print("%")
print( 'Percentage of Females is: ', FT), print("%",)



