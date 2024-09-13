dict = { "key": "value"}
print(dict["key"])
dict["key2"]=5
print(dict)
dict["key3"]=[2,4,6,7,2]
print(dict)
print("hello" in dict)
print(list(dict.keys()))
print(list(dict.values()))
print(dict)
del dict["key"]
print(dict)

for key, value in dict.items():
    print(key,value)

for key in dict:
    print(key,dict[key])
