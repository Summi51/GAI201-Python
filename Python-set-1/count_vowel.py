# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"


x="Hello"
c=0
for vawel in x:
    if vawel.lower() in 'aeiou':
        c=c+1
        print( "Number of vowels: ", c)