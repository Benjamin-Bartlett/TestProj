# Get the year given population
def getYear(popToReach):
    currentPop = 89.2
    yearDiff = 0
    while abs(currentPop-89.2) - abs(popToReach-89.2) < 0: # runs until currentPop surpasses popToReach
        yearDiff += abs(currentPop - popToReach) / -(currentPop - popToReach) # increase or decrease yearDiff by 1
        currentPop += .023 * currentPop * (abs(yearDiff) / yearDiff) # calculates the currentPop over 1 or -1 years
    return yearDiff

# get the population given the year
def getPop(years) :
    pop = 89.2
    for i in range(abs(years)):
        pop += pop * .023 * (abs(years)/years) # calculates the pop over 1 or -1 years
    return pop


# input and printing
newPop = int(input("Population: "))
print("Population in", (1990 + getYear(newPop)) , ":", getPop(int(getYear(newPop))))

yearsSince1990 = int(input("Years: "))
print("Population in", (1990 + yearsSince1990) , ":", getPop(yearsSince1990))




