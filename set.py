#set

#syntax :{}
#heter
#unordered
#unindexed
#duplicate not allowed
#set is mutable
#data is inmutable

data = {10,90.67,"hello",True,10}
print("datatype is :",type(data))
print("length is :",len(data))
print(data)
data.add(71)
print(data)
data.remove(10)
print(data)

print("data using loop")
for value in data:
    print(value)
#print(data[0])  