import math
import random

def makeRandArray():
    arr = []
    for i in range(10):
        arr.append(random.randint(1, 20))
    return arr

# Make an array size 10 filled with random numbers 1-20 (Part1)
randArray = makeRandArray()
print(randArray)

# Get Mean
mean = 0
for i in randArray:
    mean += i
mean /= len(randArray)
print("Mean : " +  str(mean))

# Get smallest value and index
smallestIndex = 0
for i in range(1, len(randArray) - 1):
    if randArray[i] < randArray[smallestIndex]:
        smallestIndex = i
print("Smallest value is " + str(randArray[smallestIndex]) + " at index " + str(smallestIndex))

# Number to Array (Part2)
num = math.floor(float(input("Number to convert: ")))
if num < 0:
    print("num must be non-negative")
    exit()

numArray = []
while num >= 1:
    numArray.insert(0, num % 10) # insert the last digit
    num //= 10 # reduce the original number
print(numArray)


# combine 2 ordered random arrays (Part3)
a = makeRandArray()
b = makeRandArray()
a.sort()
b.sort()
print(a)
print(b)


combinedArr = []
while len(combinedArr) < 20:
    if (a[0] if len(a) > 0 else 21) < (b[0] if len(b) > 0 else 21): # check which is less, accounting for outOfBounds errors
        combinedArr.append(a[0])
        a.pop(0)
    else:
        combinedArr.append(b[0])
        b.pop(0)
print(combinedArr)
