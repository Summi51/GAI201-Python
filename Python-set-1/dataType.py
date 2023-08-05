# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
#     - *Input*: None
#     - *Output*: "Type of variable1: <class 'int'>, value: 10..."


# integer
x=19;
y=33
print(x+y)
print(type)

# float
x=1.3
y=2.3;
print(y-x)
print(x-y)
print(type(x))


# string
x="Hello "
y="Masai"
print(x+y)
print(type(y))


# boolean
isTrue = True;
isFalse = False;
print(isTrue or isFalse)
print(isTrue and isFalse)
print(type(isFalse)) 
#  // output- <class 'bool'>

# list // like array
x=[1,2,3, "r", "samreen", "33", True] 
print(x)
print(x[0])
x[2]=23
print(x)
print(x.append(2300))
print(x.remove("r"))
y= [1, 2,23]
print(y)
print(y+x);
print(type(x))
#  // output- <class 'list'>

# tuple 
x=(1,2,3, "r", "samreen", "33", True)
print(x)
y=("sammi", "inayat")
x=(1,3,2)
print(y[0]+y[1])
print(x+y)
print(type(y))


# dictionary // like object
x={"name":"sammi", "age":23}
print(x)
y={"city": "PBH", "state":"UP", "isVote":True}
print(y)
print(x["name"])
print(y["isVote"])
print(type(x))


# set
x={1,2,3,4,5}
y={1, 2, 63, 54, 23, 24, 4, 5}
x.add(2)
x.add(22)
x.remove(4)
print(3 in y)
print(3 in x)
print(x)
print(type(y))
