import os
import math
# Q.69
numberOfTonsForOneFarm = 18
numberOfFarms = 30
totalNumberOfTons = numberOfFarms*numberOfTonsForOneFarm
print(str(totalNumberOfTons)+' tons')
# Q.70
initHeight = 5
initVelocity = 50
hieghtAfter3Sec = -16*(3**2)+initVelocity*3+initHeight
print(str(hieghtAfter3Sec)+' m')
# Q.71
leftTime = 5
arriveTime = 9
speed = 81.34
distance = (arriveTime-leftTime)*speed
print(str(distance)+' Km')
# Q.72
firstFillMiles = 23352
secondFillMiles = 23695
numsOfGallons = 14
differentBetween = secondFillMiles-firstFillMiles
milesPerGallon = differentBetween/numsOfGallons
print(str(milesPerGallon)+' mile/gallon')
# Q.73
numsOfWattsPerMonth = 750000000
population = 50000000
numsOfWattsDaily = int(numsOfWattsPerMonth/30)/population
print("{:,}".format(numsOfWattsDaily)+' watts/day')
# Q.74
permitOfTheDeck = 432
longOfEachSide = math.sqrt(permitOfTheDeck)
print(str(round(longOfEachSide))+' feet')
# Q.75
AccountBalance = 1000
interestRatioPerYear = 0.087
# in the first year
AccountBalance += AccountBalance*interestRatioPerYear*2
print(str(AccountBalance)+' $')
