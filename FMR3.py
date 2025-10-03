from functools import reduce

Data = [7,10,15,12,4,6,9,8.12,16]
print("Input Data :",Data)

FData = list(filter(lambda No : (No % 2 == 0),Data))
print("Filter uotput:",FData)

MData = list(map(lambda No : No+1,FData))
print("map uotput:",MData)

RData = reduce(lambda A,B: A+B,MData)
print("reduce uotput:",RData)


