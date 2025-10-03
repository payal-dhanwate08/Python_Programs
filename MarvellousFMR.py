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