# this is task 4
"""31. Binary Search
 Objective  : Implement the binary search algorithm to find a target in a sorted array.
 Input      : A sorted list of integers and a target integer.
 Output     : The index of the target or-1 if not found.
 Hint       : Use a divide-and-conquer approach by checking the middle element."""
def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low<= high :
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low = mid +1
        else:
            high = mid -1
    return -1
print(binary_search([1,2,3,4,5,6,7,33,44,55,66,76,87,99],99))
print(binary_search([1,2,3,4,5,6,7,33,44,55,66,76,87,99],98))