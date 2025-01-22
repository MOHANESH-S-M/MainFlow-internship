#this is task 2 question 12
""" 12. List Reversal
 Objective   : Reverse a given list without using built-in functions.
 Input       : A list of integers.
 Output      : Reversed list.
 Hint        : Use a loop to swap elements from start to end or slice the list ([::-1])."""
def reverse_a_list(list1):
    a=[]
    for i in range(len(list1)-1,-1,-1):
        a.append(list1[i])
    return a
print(reverse_a_list([11,22,33,44,55,66,77,88]))
