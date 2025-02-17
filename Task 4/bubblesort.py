# This is Task 4
"""30. Bubble Sort
 Objective: Implement the bubble sort algorithm to sort a list of integers.
 Input: A list of integers.
 Output: Sorted list in ascending order.
 Hint: Repeatedly swap adjacent elements if they are in the wrong order."""
def bubble_sort(list1):
    for i in range(len(list1)):
        swapped = False
        for j in range(0,len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
                swapped = True
        if swapped == False :
            break
    return list1
a = [1,3,4,2,6,3,6,2,5,6,7]
print(bubble_sort(a))