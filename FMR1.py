from functools import reduce

def CheckEven(No):
    return (No % 2 == 0)

def Increse(No):
    return No+1

def sum(A,B):
    return A+B

Data = [7,10,15,12,4,6,9,8.12,16]
print("Input Data :",Data)

FData = list(filter(CheckEven,Data))
print("Filter output:",FData)

MData = list(filter(map(Increse,FData)))
print("map output:",MData)

RData = reduce(sum,MData)
print("reduce output:",RData)


