#list

#syntax : []
#heter
#ordered
#indexed
#data mutable
#list mutable

data= [10,90.67,"hello",40,True]

print("datatype is :",type(data))
print("length is :",len(data))

print(data[0])
print(data[2])
print(data[3])
print(data[3])

data[0]=11
print(data[0])

data.append(40)
print(data(5))

print("data display using loop")
for value in data:
    print(value)
    print(data)