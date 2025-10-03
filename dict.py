#dict

#syntax : {key : value}
#heter
#ordered
#indexed (not numeric)
#key duplicate allowed but old gets overwitten
#value duplicate allowed
#data mutable (only value)

data = {"name":"let us c","Author":"Y kanetkar","price":340,"publication":"BPB publication"}

print("datatype : ",type(data))
print("length is :",len(data))
print(data)

print(data["Author"])

data["price"]=400
print(data)