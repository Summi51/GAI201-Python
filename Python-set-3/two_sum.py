# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"



def two_sum(x, target):
  for i in range(0, len(x)):
    for j in range(i+1, len(x)):
        if(x[i] + x[j] == target):
            return [i, j]

x=[2, 7, 11, 15]
target=9

print(two_sum(x, target))
