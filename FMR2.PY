from functools import reduce

CheckEven = lambda No : (No % 2 == 0)

Increse = lambda No: No+1
 
sum = lambda A,B: A+B

Data = [7,10,15,12,4,6,9,8.12,16]
print("Input Data :",Data)

FData = list(filter(CheckEven,Data))
print("Filter uotput:",FData)

MData = list(filter(map(Increse,FData)))
print("map uotput:",MData)

RData = reduce(sum,MData)
print("reduce uotput:",RData)


