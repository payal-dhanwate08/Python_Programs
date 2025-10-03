def Increase(A):
    return A+1

def Demo(Task,value):
    result = []

    for no in value:
        ret = Task(no)
        result.append(ret)

    return result

Data = [13,17,10,14,11]

RData = list(Demo(Increase,Data))

print(RData)
