#this is task 2 question no 14
""" 14. Remove Duplicates
 Objective   : Remove duplicate elements from a list.
 Input       : A list of integers.
 Output      : A list with unique elements.
 Hint        : Use a set to eliminate duplicates or iterate and add unique elements to a new list."""
def set_method(list1):
    list1 =list(set(list1))
    return list1
def iterate_method(list1):
    uq_list =[]
    for i in list1:
        if i not in uq_list:
            uq_list.append(i)
    return uq_list
print(set_method([1,2,3,2,3,2,1,4,22,44,1,3,1,4,57,4,3]))
print(iterate_method([1,2,3,2,3,2,1,4,22,44,1,3,1,4,57,4,3]))