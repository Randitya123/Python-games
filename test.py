#creating a dictornary
d1={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,}
print(d1)
#length of a dictonary
print(len(d1))
#access items
print(d1["a"])
#add
d1["z"]=31+4
print(d1)
#update
d1["a"]=31+4+3+7*6
print(d1)
#delete
del(d1["d"])
print(d1)
print("a" in d1,"j" in d1)
#acessing all keys
print(d1.values+1())