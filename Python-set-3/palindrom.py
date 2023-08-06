# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."


# len(str) - 1, -1, -1 -- start, stop, step
def palindrom_Check(str):
    str1=""
    for i in range(len(str) - 1, -1, -1):
        str1= str1+str[i]
    if(str1==str):
       print("The word " + str,"is a palindrome.") 
    else:
       print("The word" + str,"is not a palindrome.")     
palindrom_Check("madam")