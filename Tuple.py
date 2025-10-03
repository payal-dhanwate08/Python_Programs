#Tuple

#syntax : ()
#heter
#ordered
#data immutable
#tuple immutable
#duplicate

data = (10,"hello",90.67,True,10)

print("data type is :",type(data))
print("length is :",len(data))
print(data)

print(data[0])
print(data[1])

print("data using loop")
for value in data:
    print(value)

for i in range(len(data)):
    print(data[i])

#data[0]=11
#print(data[0])