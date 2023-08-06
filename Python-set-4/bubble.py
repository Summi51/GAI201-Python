# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"


#  dought
def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
    isSwap = False;
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwap = True
     
           if not isSwap:
             break;

bubble_sort([64, 34, 25, 12, 22, 11, 90])
print("Original array:", arr)
print("Sorted array:", arr)   





