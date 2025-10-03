CheckEven = lambda No : (No % 2 == 0)
Increse = lambda No: No+1
sum = lambda A,B: A+B

def filterX(Task,values):
    result = []
    for no in values:
        Ret = Task(no)
        if(Ret == True):
         result.append(no)

    return result
    
def mapX(Task,values):
    for no in values:
      result = []
      Ret = Task(no)
      result.append(Ret)

    return result

def reduceX(Task,values):
   result = 0

   for no in values:
      result = Task(result,no)

   return result   
   
def main():
Data = [7,10,15,12,4,6,9,8.12,16]
print("Input Data :",Data)

FData = list(filterX(CheckEven,Data))
print("Filter uotput:",FData)


MData = list(filter(mapX(Increse,FData)))
print("map uotput:",MData)

RData = reduceX(sum,MData)
print("reduce uotput:",RData)