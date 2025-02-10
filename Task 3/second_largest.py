#this is Task3
"""23. Find Second Largest
 Objective       : Find the second largest number in a list.
 Input           : A list of integers.
 Output          : The second largest integer.
 Hint            : Use sorting or iterate to find the largest, then the second largest."""
def second_largest_num(list1):
    if len(list1)< 2 :
        return None
    first =float('-inf')
    second = float('-inf')
    for num in list1:
        if num> first:
            second = first
            first = num
        elif num> second and num != first :
            second = num
    return second if second != float('-inf') else None
a = [2,3,4,5,6,7,8,9]
print(second_largest_num(a))
