# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."


x=[1,2,3,4,5,6,7,8,9,10,20]
# add
x[2]=33;
print(x)
# append/add
x.append(56)
print(x)
# remove
x.remove(9)
print(x)
# sort
x.sort()   
print(x)